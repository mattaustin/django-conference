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
from .models import Conference, Presenter, Resource, TimeSlot, Venue
from django.contrib import admin


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):

    fields = [('name', 'slug'), 'city', ('start_date', 'end_date'), 'venues']

    prepopulated_fields = {'slug': ['name']}


@admin.register(Presenter)
class PresenterAdmin(admin.ModelAdmin):

    fields = ['name', 'biography', 'email', 'blog', 'twitter_handle',
              'irc_handle', 'github_handle', 'slack_handle',
              ('business', 'position')]


class ResourceInline(admin.TabularInline):

    fields = ['name', 'venue']

    model = Resource


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):

    fields = ['conference', 'name', 'description', ('start_at', 'end_at'),
              'presenters', 'resources', 'video', 'slides']

    list_display = ['name', 'conference', 'start_at', 'end_at']

    list_filter = ['conference', 'presenters', 'resources']


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):

    fields = ['name']

    inlines = [ResourceInline]
