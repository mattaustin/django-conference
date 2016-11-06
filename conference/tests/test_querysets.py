# -*- coding: utf-8 -*-
#
# Copyright 2016 Matt Austin
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import, unicode_literals
from conference.factories import TimeSlotFactory
from conference.models import TimeSlot
from dateutil.relativedelta import relativedelta
from django.test import TestCase
from django.utils import timezone
from freezegun import freeze_time

try:  # Python 3
    from unittest import mock
except ImportError:  # Python 2
    import mock


class TestLotteryQuerySetPastFilter(TestCase):

    def setUp(self):
        self.now = timezone.pytz.timezone('Atlantic/Azores').localize(
            timezone.datetime(2016, 1, 2, 11, 12))

    def test_includes_a_timeslot_which_ended_yesterday(self):
        timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=-26),
            end_at=self.now + relativedelta(hours=-25))

        with freeze_time(self.now):
            queryset = TimeSlot.objects.past()

        self.assertIn(timeslot, queryset)

    def test_excludes_a_timeslot_which_is_starting_now(self):
        timeslot = TimeSlotFactory(
            start_at=self.now,
            end_at=self.now + relativedelta(hours=+1))

        with freeze_time(self.now):
            queryset = TimeSlot.objects.past()

        self.assertNotIn(timeslot, queryset)

    def test_excludes_a_timeslot_which_is_happening_now(self):
        timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=-0.5),
            end_at=self.now + relativedelta(hours=+0.5))

        with freeze_time(self.now):
            queryset = TimeSlot.objects.past()

        self.assertNotIn(timeslot, queryset)

    def test_includes_a_timeslot_which_has_ended_now(self):
        timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=-1),
            end_at=self.now)

        with freeze_time(self.now):
            queryset = TimeSlot.objects.past()

        self.assertIn(timeslot, queryset)

    def test_excludes_a_timeslot_which_starts_tomorrow(self):
        timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=+24),
            end_at=self.now + relativedelta(hours=+25))

        with freeze_time(self.now):
            queryset = TimeSlot.objects.past()

        self.assertNotIn(timeslot, queryset)


class TestLotteryQuerySetCurrentFilter(TestCase):

    def setUp(self):
        self.now = timezone.pytz.timezone('Atlantic/Azores').localize(
            timezone.datetime(2016, 1, 2, 11, 12))

    def test_excludes_a_timeslot_which_ended_yesterday(self):
        timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=-26),
            end_at=self.now + relativedelta(hours=-25))

        with freeze_time(self.now):
            queryset = TimeSlot.objects.current()

        self.assertNotIn(timeslot, queryset)

    def test_includes_a_timeslot_which_is_starting_now(self):
        timeslot = TimeSlotFactory(
            start_at=self.now,
            end_at=self.now + relativedelta(hours=+1))

        with freeze_time(self.now):
            queryset = TimeSlot.objects.current()

        self.assertIn(timeslot, queryset)

    def test_includes_a_timeslot_which_is_happening_now(self):
        timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=-0.5),
            end_at=self.now + relativedelta(hours=+0.5))

        with freeze_time(self.now):
            queryset = TimeSlot.objects.current()

        self.assertIn(timeslot, queryset)

    def test_excludes_a_timeslot_which_has_ended_now(self):
        timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=-1),
            end_at=self.now)

        with freeze_time(self.now):
            queryset = TimeSlot.objects.current()

        self.assertNotIn(timeslot, queryset)

    def test_excludes_a_timeslot_which_starts_tomorrow(self):
        timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=+24),
            end_at=self.now + relativedelta(hours=+25))

        with freeze_time(self.now):
            queryset = TimeSlot.objects.current()

        self.assertNotIn(timeslot, queryset)


class TestLotteryQuerySetFutureFilter(TestCase):

    def setUp(self):
        self.now = timezone.pytz.timezone('Atlantic/Azores').localize(
            timezone.datetime(2016, 1, 2, 11, 12))

    def test_excludes_a_timeslot_which_ended_yesterday(self):
        timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=-26),
            end_at=self.now + relativedelta(hours=-25))

        with freeze_time(self.now):
            queryset = TimeSlot.objects.future()

        self.assertNotIn(timeslot, queryset)

    def test_excludes_a_timeslot_which_is_starting_now(self):
        timeslot = TimeSlotFactory(
            start_at=self.now,
            end_at=self.now + relativedelta(hours=+1))

        with freeze_time(self.now):
            queryset = TimeSlot.objects.future()

        self.assertNotIn(timeslot, queryset)

    def test_excludes_a_timeslot_which_is_happening_now(self):
        timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=-0.5),
            end_at=self.now + relativedelta(hours=+0.5))

        with freeze_time(self.now):
            queryset = TimeSlot.objects.future()

        self.assertNotIn(timeslot, queryset)

    def test_excludes_a_timeslot_which_has_ended_now(self):
        timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=-1),
            end_at=self.now)

        with freeze_time(self.now):
            queryset = TimeSlot.objects.future()

        self.assertNotIn(timeslot, queryset)

    def test_includes_a_timeslot_which_starts_tomorrow(self):
        timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=+24),
            end_at=self.now + relativedelta(hours=+25))

        with freeze_time(self.now):
            queryset = TimeSlot.objects.future()

        self.assertIn(timeslot, queryset)


class TestLotteryQuerySetNowFilter(TestCase):

    def setUp(self):
        self.now = timezone.pytz.timezone('Atlantic/Azores').localize(
            timezone.datetime(2016, 1, 2, 11, 12))
        self.earlier_timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=-2),
            end_at=self.now + relativedelta(hours=-1))
        self.now_timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=-0.5),
            end_at=self.now + relativedelta(hours=+0.5))
        self.later_timeslot = TimeSlotFactory(
            start_at=self.now + relativedelta(hours=+1),
            end_at=self.now + relativedelta(hours=+2))

    def test_calls_current(self):
        queryset = TimeSlot.objects.all()
        with mock.patch.object(queryset, 'current', mock.Mock()):
            queryset.now()
            self.assertTrue(queryset.current.called)

    def test_returns_now_timeslot(self):
        with freeze_time(self.now):
            now = TimeSlot.objects.now()

        self.assertEqual(self.now_timeslot, now)

    def test_does_not_return_later_timeslot(self):
        with freeze_time(self.now):
            now = TimeSlot.objects.now()

        self.assertNotEqual(self.later_timeslot, now)

    def test_does_not_return_earlier_timeslot(self):
        with freeze_time(self.now):
            now = TimeSlot.objects.now()

        self.assertNotEqual(self.earlier_timeslot, now)

    def test_returns_none_when_no_now_timeslot(self):
        with freeze_time(self.now + relativedelta(days=+1)):
            now = TimeSlot.objects.now()

        self.assertIsNone(now)


class TestLotteryQuerySetNextFilter(TestCase):

    def setUp(self):
        self.today = timezone.pytz.timezone('Atlantic/Azores').localize(
            timezone.datetime(2016, 1, 2, 11, 12))
        self.earlier_today_timeslot = TimeSlotFactory(
            start_at=self.today + relativedelta(hours=-2),
            end_at=self.today + relativedelta(hours=-1))
        self.later_today_timeslot = TimeSlotFactory(
            start_at=self.today + relativedelta(hours=+1),
            end_at=self.today + relativedelta(hours=+2))
        self.tomorrow = self.today + relativedelta(days=+1)
        self.later_tomorrow_timeslot = TimeSlotFactory(
            start_at=self.tomorrow + relativedelta(hours=+1),
            end_at=self.tomorrow + relativedelta(hours=+2))

    def test_calls_future(self):
        queryset = TimeSlot.objects.all()
        with mock.patch.object(queryset, 'future', mock.Mock()):
            queryset.next()
            self.assertTrue(queryset.future.called)

    def test_excludes_earlier_today_timeslot_when_today(self):
        with freeze_time(self.today):
            next = TimeSlot.objects.next()

        self.assertNotEqual(self.earlier_today_timeslot, next)

    def test_returns_later_today_timeslot_when_today(self):
        with freeze_time(self.today):
            next = TimeSlot.objects.next()

        self.assertEqual(self.later_today_timeslot, next)

    def test_does_not_return_later_tomorrow_timeslot_when_today(self):
        with freeze_time(self.today):
            next = TimeSlot.objects.next()

        self.assertNotEqual(self.later_tomorrow_timeslot, next)

    def test_does_not_return_later_today_timeslot_when_tomorrow(self):
        with freeze_time(self.tomorrow):
            next = TimeSlot.objects.next()

        self.assertNotEqual(self.later_today_timeslot, next)

    def test_returns_later_tomorrow_timeslot_when_tomorrow(self):
        with freeze_time(self.tomorrow):
            next = TimeSlot.objects.next()

        self.assertEqual(self.later_tomorrow_timeslot, next)

    def test_returns_none_when_no_next_timeslot(self):
        with freeze_time(self.tomorrow + relativedelta(days=+1)):
            next = TimeSlot.objects.next()

        self.assertIsNone(next)


class TestLotteryQuerySetLaterFilter(TestCase):

    def setUp(self):
        self.today = timezone.pytz.timezone('Atlantic/Azores').localize(
            timezone.datetime(2016, 1, 2, 11, 12))
        self.earlier_today_timeslot = TimeSlotFactory(
            start_at=self.today + relativedelta(hours=-2),
            end_at=self.today + relativedelta(hours=-1))
        self.later_today_timeslot = TimeSlotFactory(
            start_at=self.today + relativedelta(hours=+1),
            end_at=self.today + relativedelta(hours=+2))
        self.tomorrow = self.today + relativedelta(days=+1)
        self.later_tomorrow_timeslot = TimeSlotFactory(
            start_at=self.tomorrow + relativedelta(hours=+1),
            end_at=self.tomorrow + relativedelta(hours=+2))

    def test_calls_future(self):
        queryset = TimeSlot.objects.all()
        with mock.patch.object(queryset, 'future', mock.MagicMock()):
            queryset.later()
            self.assertTrue(queryset.future.called)

    def test_excludes_earlier_today_timeslot_when_today(self):
        with freeze_time(self.today):
            later = TimeSlot.objects.later()

        self.assertNotEqual(self.earlier_today_timeslot, later)

    def test_does_not_return_later_today_timeslot_when_today(self):
        with freeze_time(self.today):
            later = TimeSlot.objects.later()

        self.assertNotEqual(self.later_today_timeslot, later)

    def test_returns_later_tomorrow_timeslot_when_today(self):
        with freeze_time(self.today):
            later = TimeSlot.objects.later()

        self.assertEqual(self.later_tomorrow_timeslot, later)

    def test_returns_none_when_no_later_timeslot(self):
        with freeze_time(self.tomorrow):
            later = TimeSlot.objects.later()

        self.assertIsNone(later)
