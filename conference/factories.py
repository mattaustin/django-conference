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
from django.utils import timezone

try:
    import factory
except ImportError as e:
    raise ImportError('The package "factory-boy" is required.')
else:
    from factory import fuzzy


class ConferenceFactory(factory.django.DjangoModelFactory):

    name = factory.Sequence(lambda n: 'Conference {}'.format(n))

    slug = factory.Sequence(lambda n: 'conference-{}'.format(n))

    class Meta(object):
        model = 'conference.Conference'


class TimeSlotFactory(factory.django.DjangoModelFactory):

    conference = factory.SubFactory('conference.factories.ConferenceFactory')

    name = factory.Sequence(lambda n: 'Time Slot {}'.format(n))

    start_at = fuzzy.FuzzyDateTime(
        timezone.pytz.timezone('UTC').localize(timezone.datetime(2000, 1, 1)),
        timezone.pytz.timezone('UTC').localize(timezone.datetime(2020, 1, 1)))

    end_at = factory.LazyAttribute(
        lambda o: o.start_at + timezone.timedelta(hours=1))

    class Meta(object):
        model = 'conference.TimeSlot'


class VenueFactory(factory.django.DjangoModelFactory):

    name = factory.Sequence(lambda n: 'Venue {}'.format(n))

    class Meta(object):
        model = 'conference.Venue'
