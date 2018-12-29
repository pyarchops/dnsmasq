#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import codecs
import os
import re
from setuptools import setup


HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """ reads parts """
    with codecs.open(os.path.join(HERE, *parts), 'r') as blob:
        return blob.read()


def find_version(*file_paths):
    """ finds __version___ in __init__.py files """
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open('README.rst') as readme_file:
    README = readme_file.read()

with open('HISTORY.rst') as history_file:
    HISTORY = history_file.read()

with open('requirements.txt') as requirements_file:
    REQUIREMENTS = requirements_file.read().splitlines()

SETUP_REQUIREMENTS = ['pytest-runner', ]

with open('requirements_dev.txt') as requirements_dev_file:
    TEST_REQUIREMENTS = requirements_dev_file.read().splitlines()

setup(
    name='pyarchops_dnsmasq',
    author="Azul",
    author_email='pyarchops@azulinho.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    description="Install All dnsmasq",
    install_requires=REQUIREMENTS,
    license="MIT license",
    long_description=README + '\n\n' + HISTORY,
    include_package_data=True,
    keywords='pyarchops_dnsmasq',
    packages=['pyarchops_dnsmasq'],
    setup_requires=SETUP_REQUIREMENTS,
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
    url='https://github.com/pyarchops/dnsmasq',
    version=find_version('pyarchops_dnsmasq', '__init__.py'),
    zip_safe=False,
)
