#
# Copyright (c) 2017, Magenta ApS
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#

from setuptools import setup
from setuptools import find_packages

setup(
    name='lora_utils',
    version='0.1.0',
    description='',
    author='Magenta ApS',
    author_email='info@magenta.dk',
    license="MPL 2.0",
    packages=find_packages(exclude=['tests']),
    package_data={
        '': ["*.txt", "*.xml"]
    },
    zip_safe=False,
    install_requires=[
        "python3-saml>=1.4",
        "flask>=1.0",
        "Flask-Session>=0.3",
        "requests>=2.19",
        "Flask-SQLAlchemy>=2.3",
        "itsdangerous>=1.1",
        'mock>=3.0.5',
    ],
    tests_require=[
        'Flask-Testing',
        'freezegun',
        'werkzeug<1.0.0'
    ]
)