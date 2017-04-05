# -*- coding: utf-8 -*-
import logging
from smtplib import SMTPException

from django.core.mail import send_mail
from django.core.management import call_command
from django.conf import settings
from django.db.models import Q

from pdfgen.certificate import CertPDFException, CertPDFUserNotFoundException
from pdfgen.views import CertException
from lms import CELERY_APP
from opaque_keys.edx.keys import CourseKey
from certificates.models import CertificateStatuses, GeneratedCertificate
from courseware.courses import get_course_by_id
from courseware.views import is_course_passed
from student.models import CourseEnrollment, UserStanding
from xmodule.modulestore.django import modulestore
from ga_operation.utils import (delete_files, change_behavior_sys,
                                get_std_info_from_local_storage, handle_uploaded_generated_file_to_s3)

log = logging.getLogger(__name__)


class TaskBase(object):
    """ Each Task Class's BaseClass """

    def __init__(self, email):
        super(TaskBase, self).__init__()
        self.err_msg = ''
        self.out_msg = ''
        self.email = email

    def _send_email(self):
        try:
            subject, body = self._get_email_subject(), self._get_email_body()
            send_mail(subject,
                      body,
                      settings.GA_OPERATION_EMAIL_SENDER,
                      [self.email],
                      fail_silently=False)
        except SMTPException:
            log.warning("Failure sending e-mail address: {}".format(self.email))
            log.exception("Failed to send a email to a staff.")
        except Exception as e:
            log.exception('Caught the exception: ' + type(e).__name__)

    def _get_email_subject(self):
        if self.err_msg:
            return "{} was failure".format(self.get_command_name())
        else:
            return "{} was completed.".format(self.get_command_name())

    def _get_email_body(self):
        if self.err_msg:
            return self.err_msg
        else:
            return "{} was succeeded.\n\n{}".format(self.get_command_name(), self.out_msg)

    @staticmethod
    def get_command_name():
        raise NotImplementedError


@CELERY_APP.task
def create_certs_task(course_id, email, student_ids, prefix=""):
    """create_certs_task main."""
    CreateCerts(course_id, email, student_ids, prefix).run()


class CreateCerts(TaskBase):
    """Generate certificate class"""

    def __init__(self, course_id, email, student_ids, prefix):
        super(CreateCerts, self).__init__(email)
        self.student_ids = student_ids
        self.prefix = prefix
        self.course_id = course_id
        self.operation = "create"

    def run(self):
        try:
            if self.student_ids:
                for student in self.student_ids:
                    try:
                        call_command(
                            self.get_command_name(), self.operation, self.course_id,
                            username=student, debug=False, noop=False, prefix=self.prefix
                        )
                    except CertPDFUserNotFoundException:
                        # continue the process when got error that not found certificate user.
                        log.warning("User({}) was not found".format(student))
                        continue
            else:
                call_command(self.get_command_name(),
                             self.operation, self.course_id,
                             username=False, debug=False, noop=False, prefix=self.prefix)
        except (CertException, CertPDFException) as e:
            msg = 'Failure to generate the PDF files from create_certs command.'
            log.exception(msg)
            self.err_msg = "{} {}".format(msg, e)
        except Exception as e:
            msg = 'Caught the exception: ' + type(e).__name__
            log.exception(msg)
            self.err_msg = "{} {}".format(msg, e)
        finally:
            self._send_email()

    def _get_email_body(self):
        if self.err_msg:
            return "{}({}) was failed.\n\n{}".format(self.get_command_name(),
                                                     self.operation,
                                                     self.err_msg)
        else:
            all_certs = GeneratedCertificate.objects.filter(
                course_id=CourseKey.from_string(self.course_id),
                status=CertificateStatuses.generating).order_by('id')
            if self.student_ids:
                # When specifying a target, separate the URL we created now and all the already created URLs.
                created_certs = GeneratedCertificate.objects.filter(
                    Q(course_id=CourseKey.from_string(self.course_id)),
                    Q(user__email__in=self.student_ids) | Q(user__username__in=self.student_ids),
                    Q(status=CertificateStatuses.generating)).order_by('id')

                created_message = u"{}件の修了証を発行しました\n{}\n\n".format(
                    len(created_certs), "\n".join([gc.download_url for gc in created_certs]))
                all_message = u"{}件の修了証はまだ公開されていません\n{}".format(
                    len(all_certs), "\n".join([gc.download_url for gc in all_certs]))
                return created_message + all_message
            else:
                return self._get_email_body_for_all_certs(all_certs)

    def _get_email_body_for_all_certs(self, all_certs):
        def _get_unenroll_username_list(_course_key):
            return [
                enrollment.user.username for enrollment in CourseEnrollment.objects.filter(
                    course_id=_course_key, is_active=False)
            ]

        def _get_disabled_account_list(_course_key):
            return [
                userstanding.user.username for userstanding in UserStanding.objects.filter(
                    user__in=[c.user for c in CourseEnrollment.objects.filter(course_id=_course_key)],
                    account_status=UserStanding.ACCOUNT_DISABLED
                )
            ]

        def _get_not_activate_and_course_passed_username_list(_course_key):
            return [
                enrollment.user.username for enrollment in CourseEnrollment.objects.filter(course_id=_course_key)
                if not enrollment.user.is_active and is_course_passed(
                    course=get_course_by_id(course_key=_course_key),
                    student=enrollment.user
                )
            ]

        course_key = CourseKey.from_string(self.course_id)
        unenroll_username_list = _get_unenroll_username_list(course_key)
        disabled_username_list = _get_disabled_account_list(course_key)
        not_activate_username_list = _get_not_activate_and_course_passed_username_list(course_key)

        return (
            u"修了証発行数： {all_certs_count}\n"
            u"※受講解除者{unenroll_count}人を含みます（受講解除ユーザー名：{unenroll_username_list}）\n"
            u"※退会者{disabled_account_count}人を含みます（退会ユーザー名：{disabled_username_list}）\n"
            u"---\n"
            u"修了判定データに含まれる合格かつ未アクティベート者数：{not_activate_username_count}（未アクティベートユーザー名：{not_activate_username_list}）\n"
            u"\n"
            u"---\n{cert_list}"
        ).format(
            all_certs_count=len(all_certs),
            unenroll_count=len(unenroll_username_list),
            unenroll_username_list=", ".join(unenroll_username_list),
            disabled_account_count=len(disabled_username_list),
            disabled_username_list=", ".join(disabled_username_list),
            not_activate_username_count=len(not_activate_username_list),
            not_activate_username_list=", ".join(not_activate_username_list),
            cert_list="\n".join([gc.download_url for gc in all_certs]),
        )

    def _get_email_subject(self):
        if self.err_msg:
            return "{} was failure ({})".format(self.get_command_name(), self.course_id)
        else:
            return "{} was completed. ({})".format(self.get_command_name(), self.course_id)

    @staticmethod
    def get_command_name():
        return "create_certs"


@CELERY_APP.task
def dump_oa_scores_task(course_id, email):
    """dump_oa_scores_task main."""
    DumpOaScores(course_id, email).run()


class DumpOaScores(TaskBase):
    """DumpOaScores class."""

    def __init__(self, course_id, email):
        super(DumpOaScores, self).__init__(email)
        self.course_id = course_id

    def run(self):
        oa_items = None
        try:
            course_key = CourseKey.from_string(self.course_id)
            oa_items = modulestore().get_items(course_key, qualifiers={'category': 'openassessment'})
            with change_behavior_sys():
                # Change behavior raw_input method while take the all dump files
                # The raw_input's behavior has been changed and if call it, return the increment value.
                for _ in range(0, len(oa_items)):
                    call_command(self.get_command_name(), self.course_id, dump_dir=self._get_dump_dir())
        except Exception as e:
            log.exception('Caught the exception: ' + type(e).__name__)
        finally:
            if oa_items:
                self.err_msg, self.out_msg = get_std_info_from_local_storage()
                self._send_email()

    @staticmethod
    def _get_dump_dir():
        return settings.GA_OPERATION_WORK_DIR + "/" + DumpOaScores.get_command_name()

    @staticmethod
    def get_command_name():
        return "dump_oa_scores"


@CELERY_APP.task
def ga_get_grades_g1528_task(course_list, email):
    """ga_get_grades_g1528_task main."""
    GaGetGradesG1528(course_list, email).run()


class GaGetGradesG1528(TaskBase):
    """GaGetGradesG1528 class."""
    def __init__(self, course_list, email):
        super(GaGetGradesG1528, self).__init__(email)
        self.course_list = course_list

    def run(self):
        file_path_list = []
        try:
            file_path = self._get_output_file_path()
            with change_behavior_sys():
                call_command(self.get_command_name(), *self.course_list,
                             output=file_path,
                             sitename=self._get_company_key()["site_name"])
            file_path_list = handle_uploaded_generated_file_to_s3(
                [file_path],
                self._get_company_key()["bucket_name"]
            )
        except Exception as e:
            log.exception('Caught the exception: ' + type(e).__name__)
            self.err_msg = "{}".format(e)
        finally:
            if not self.err_msg:
                self.err_msg, self.out_msg = get_std_info_from_local_storage()
            self.out_msg += '\n'.join(file_path_list)
            self._send_email()
            delete_files([self._get_company_key()["output_file_name"]], settings.GA_OPERATION_WORK_DIR)

    def _get_output_file_path(self):
        return settings.GA_OPERATION_WORK_DIR + '/' + self._get_company_key()["output_file_name"]

    @staticmethod
    def _get_company_key():
        return settings.GA_OPERATION_SPECIFIC_COMPANY_KEYS["g1528"]

    @staticmethod
    def get_command_name():
        return "ga_get_grades"
