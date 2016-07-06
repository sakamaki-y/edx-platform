# -*- coding: utf-8 -*-
import re

from django import forms
from django.conf import settings

from opaque_keys import InvalidKeyError
from opaque_keys.edx.keys import CourseKey


class GaOperationBaseForm(forms.Form):
    course_id = forms.CharField(required=True)

    def clean_course_id(self):
        val = self.cleaned_data.get('course_id')
        try:
            CourseKey.from_string(val)
        except InvalidKeyError:
            raise forms.ValidationError(u"講座IDの書式が不正です。")
        return val


class GaOperationEmailField(forms.EmailField):
    def clean(self, value):
        super(GaOperationEmailField, self).clean(value)
        # permit valid domains only.
        for domain in settings.GA_OPERATION_VALID_DOMAINS_LIST:
            if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@{}$'.format(domain), value):
                return value
        raise forms.ValidationError(u"このドメインのEメールは使用できません。")