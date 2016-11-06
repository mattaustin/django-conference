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


from __future__ import print_function
from conference import __title__, __url__, __version__
from setuptools import setup, find_packages
import os


def read(fname):
    # https://pythonhosted.org/an_example_pypi_project/setuptools.html#setting-up-setup-py
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name=__title__,
    version=__version__,

    # Packaging
    packages=find_packages(exclude=['docs']),
    include_package_data=True,

    # Dependencies
    install_requires=[],

    # Author information
    author='Matt Austin',
    author_email='mail@mattaustin.me.uk',

    # Additional information
    url=__url__,
    license='Apache Software License 2.0',
    description='A reusable django application providing models and views for '
                'a simple conference.',
    long_description=read('README.rst'),
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
    ],
)
