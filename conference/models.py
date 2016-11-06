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
from . import querysets
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import uuid


@python_2_unicode_compatible
class Conference(models.Model):

    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4,
                          editable=False)

    name = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    city = models.CharField(max_length=200, blank=True, default='')

    start_date = models.DateField(blank=True, null=True)

    end_date = models.DateField(blank=True, null=True)

    venues = models.ManyToManyField('conference.Venue', blank=True)

    class Meta(object):
        default_related_name = 'conferences'
        ordering = ['start_date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('conference:conference_detail',
                       kwargs={'slug': self.slug})


@python_2_unicode_compatible
class Presenter(models.Model):

    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4,
                          editable=False)

    name = models.CharField(max_length=200)

    biography = models.TextField(blank=True, default='')

    email = models.EmailField(blank=True, default='')

    blog = models.URLField(blank=True, default='')

    twitter_handle = models.CharField(max_length=50, blank=True, default='')

    irc_handle = models.CharField('IRC handle', max_length=50, blank=True,
                                  default='')

    github_handle = models.CharField(max_length=50, blank=True, default='')

    slack_handle = models.CharField(max_length=50, blank=True, default='')

    business = models.CharField(max_length=200, blank=True, default='')

    position = models.CharField(max_length=200, blank=True, default='')

    class Meta(object):
        default_related_name = 'presenters'
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Resource(models.Model):

    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4,
                          editable=False)

    name = models.CharField(max_length=200)

    venue = models.ForeignKey('conference.Venue', on_delete=models.PROTECT)

    class Meta(object):
        default_related_name = 'resources'
        ordering = ['name']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class TimeSlot(models.Model):
    """A timeslot, typically representing a session/presentation at the
    conference.

    """

    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4,
                          editable=False)

    conference = models.ForeignKey('conference.Conference',
                                   on_delete=models.PROTECT)

    name = models.CharField(max_length=200)

    description = models.TextField(blank=True, default='')

    start_at = models.DateTimeField()

    end_at = models.DateTimeField()

    presenters = models.ManyToManyField('conference.Presenter', blank=True)

    resources = models.ManyToManyField('conference.Resource', blank=True)

    video = models.URLField(blank=True, default='')

    slides = models.FileField(max_length=250, upload_to='slides', blank=True,
                              null=True)

    objects = querysets.TimeSlotQuerySet.as_manager()

    class Meta(object):
        default_related_name = 'timeslots'
        ordering = ['start_at']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Venue(models.Model):

    id = models.UUIDField('ID', primary_key=True, default=uuid.uuid4,
                          editable=False)

    name = models.CharField(max_length=200)

    address = models.TextField(blank=True, default='')

    class Meta(object):
        default_related_name = 'venues'
        ordering = ['name']

    def __str__(self):
        return self.name
