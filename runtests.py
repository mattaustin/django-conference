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
from django.conf import settings
from django.test.utils import get_runner
import sys


settings.configure(
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'conference',
    ],
)


try:
    import django
    setup = django.setup
except AttributeError:
    pass
else:
    setup()


def run_tests(*test_args):
    if not test_args:
        test_args = ['conference.tests']

    # Run tests
    TestRunner = get_runner(settings)
    test_runner = TestRunner()

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(bool(failures))


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
