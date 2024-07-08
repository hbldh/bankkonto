#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The setup script for the Bankkonto package.

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>

Created on 2017-02-15

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import sys
import re
from codecs import open

from setuptools import setup, find_packages

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist upload')
    sys.exit()

with open('bankkonto/version.py', 'r') as fd:
    _version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE)
    assert _version
    version = _version.group(1)


def read(f: str) -> str:
    return open(f, encoding='utf-8').read()


setup(
    name='bankkonto',
    version=version,
    author='Henrik Blidh',
    author_email='henrik.blidh@swedwise.com',
    url='https://github.com/hbldh/bankkonto',
    description="Python validation library for Swedish bank account numbers",
    long_description=read('README.rst') + '\n\n' + read('HISTORY.rst'),
    license='MIT',
    platforms='any',
    keywords=['Bank', 'Bank account', 'Swedish bank account', 'validation'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Telecommunications Industry',
        'Topic :: Office/Business :: Financial',
    ],
    packages=find_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    package_data={
        'bankkonto': ['py.typed'],
    },
    install_requires=[],
    extras_require={},
    ext_modules=[],
    entry_points={
        'console_scripts': [
            'bankkonto-validate = bankkonto:cli',
        ],
    }
)
