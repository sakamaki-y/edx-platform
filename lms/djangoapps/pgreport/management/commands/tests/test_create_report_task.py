from django.test import TestCase
from django.core.management.base import CommandError
from mock import patch
from pgreport.management.commands import create_report_task as ct 


class CreateReportTaskCommandTestCase(TestCase):
    """For unit test."""

    def setUp(self):
        self.args_create = ["create"]
        self.args_status = ["status"]
        self.args_list = ["list"]
        self.args_revoke = ["revoke"]
        self.options_course_id = {'course_id': "org/num/run", 'task_id': None}
        self.options_task_id = {'course_id': None, 'task_id': "dummy_task_id"}
        self.options_none = {'course_id': None, 'task_id': None}

    def tearDown(self):
        pass

    @patch('pgreport.management.commands.create_report_task.check_course_id')
    @patch('pgreport.management.commands.create_report_task.ProgressReportTask')
    def test_handle(self, pg_mock, check_mock):
        ct.Command().handle(*self.args_create, **self.options_course_id)
        pg_mock().send_task.assert_called_once_with(self.options_course_id["course_id"])

        ct.Command().handle(*self.args_status, **self.options_task_id)
        pg_mock().show_task_status.assert_called_once_with(self.options_task_id["task_id"])

        ct.Command().handle(*self.args_list, **self.options_none)
        pg_mock().show_task_list.assert_called_once_with()

        ct.Command().handle(*self.args_revoke, **self.options_task_id)
        pg_mock().revoke_task.assert_called_once_with(self.options_task_id["task_id"])

        msg = '^Required subcommand, create, list, status or revoke.$'
        with self.assertRaisesRegexp(CommandError, msg):
            ct.Command().handle(*[], **self.options_course_id)

        msg = '^"status" subcommand required task_id.$'
        with self.assertRaisesRegexp(CommandError, msg):
            ct.Command().handle(*self.args_status, **self.options_none)

        msg = '^"revoke" subcommand required task_id.$'
        with self.assertRaisesRegexp(CommandError, msg):
            ct.Command().handle(*self.args_revoke, **self.options_none)

        msg = '^"create" subcommand required course_id.$'
        with self.assertRaisesRegexp(CommandError, msg):
            ct.Command().handle(*self.args_create, **self.options_none)

        msg = '^Invalid subcommand.$'
        with self.assertRaisesRegexp(CommandError, msg):
            ct.Command().handle(*["wrong"], **self.options_course_id)