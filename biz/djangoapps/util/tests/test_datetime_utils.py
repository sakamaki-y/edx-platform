"""
Tests for datetime_utils
"""

from datetime import datetime, date
from mock import patch
import pytz

from django.conf import settings
from django.test.utils import override_settings

from biz.djangoapps.util import datetime_utils
from biz.djangoapps.util.tests.testcase import BizTestBase


class DateTimeUtilsTest(BizTestBase):

    def setUp(self):
        from django.utils import timezone
        # _localtime is global property. Clear it because it may have been set by the other testcase.
        timezone._localtime = None
        super(DateTimeUtilsTest, self).setUp()

    @override_settings(TIME_ZONE='Asia/Tokyo')
    def test_timezone_now(self):
        _timezone = pytz.timezone('Asia/Tokyo')
        with patch(
            'django.utils.timezone.now',
            side_effect=lambda: datetime(2015, 12, 31, 15, 0, 0).replace(tzinfo=pytz.utc)
        ):
            now = datetime_utils.timezone_now()
            self.assertEqual(datetime(2016, 1, 1, 0, 0, 0, tzinfo=_timezone), now)
            self.assertEqual(_timezone, now.tzinfo)

    @override_settings(TIME_ZONE='Asia/Tokyo')
    def test_timezone_today(self):
        with patch(
            'django.utils.timezone.now',
            side_effect=lambda: datetime(2015, 12, 31, 15, 0, 0).replace(tzinfo=pytz.utc)
        ):
            self.assertEqual(date(2016, 1, 1), datetime_utils.timezone_today())

    @override_settings(TIME_ZONE='Asia/Tokyo')
    def test_to_jst(self):
        _timezone = pytz.timezone('Asia/Tokyo')
        self.assertEqual(
            datetime(2015, 12, 31, 15, 0, 0),
            datetime_utils.to_jst(datetime(2015, 12, 31, 15, 0, 0))
        )
        self.assertEqual(
            datetime(2015, 12, 31, 15, 0, 0, tzinfo=pytz.utc),
            datetime_utils.to_jst(datetime(2016, 1, 1, 0, 0, 0, tzinfo=pytz.timezone('Asia/Tokyo')))
        )

    def test_format_for_w2ui(self):
        # datetime (has timezone)
        self.assertEqual(
            '2016/01/01 12:34:56 JST',
            datetime_utils.format_for_w2ui(datetime(2016, 1, 1, 12, 34, 56, tzinfo=pytz.timezone('Asia/Tokyo')))
        )
        # datetime (no timezone)
        self.assertEqual(
            '2016/01/01 12:34:56',
            datetime_utils.format_for_w2ui(datetime(2016, 1, 1, 12, 34, 56))
        )
        # date
        self.assertEqual(
            '2016/01/01',
            datetime_utils.format_for_w2ui(date(2016, 1, 1))
        )
        # other type
        with self.assertRaises(TypeError):
            datetime_utils.format_for_w2ui('2016-01-01')