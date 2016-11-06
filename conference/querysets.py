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
from django.db import models
from django.utils import timezone


class TimeSlotQuerySet(models.query.QuerySet):
    """Customised :py:class:`~django.db.models.db.query.QuerySet` for
    :py:class:`~conference.models.TimeSlot` model."""

    def past(self):
        """Filter for time slots in the past.

        :returns: Filtered queryset.
        :rtype: :py:class:`.TimeSlotQuerySet`
        """
        now = timezone.now()
        return self.filter(end_at__lte=now)

    def current(self):
        """Filter for time slots happening now.

        :returns: Filtered queryset.
        :rtype: :py:class:`.TimeSlotQuerySet`
        """
        now = timezone.now()
        return self.filter(start_at__lte=now, end_at__gt=now)

    def future(self):
        """Filter for future time slots.

        :returns: Filtered queryset.
        :rtype: :py:class:`.TimeSlotQuerySet`
        """
        now = timezone.now()
        return self.filter(start_at__gt=now)

    def now(self):
        """Filter for the next future time slot.

        :returns: Time slot instance.
        :rtype: :py:class:`~conference.models.TimeSlot`
        """
        return self.current().first()

    def next(self):
        """Filter for the next future time slot.

        :returns: Time slot instance.
        :rtype: :py:class:`~conference.models.TimeSlot`
        """
        return self.future().first()

    def later(self):
        """Filter for the next+1 future time slot.

        :returns: Time slot instance.
        :rtype: :py:class:`~conference.models.TimeSlot`
        """
        queryset = self.future()[1:2]
        if queryset:
            return queryset[0]
