#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Bankkonto
=========

TBW

"""
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import re

from .version import __version__, version
from .exceptions import BankkontoException, BankkontoValidationError
from .account import validate


def clean_and_split(bank_account_number):
    cleaned = re.sub('\D', '', bank_account_number)
    if cleaned.startswith('8'):
        # Swedbank accounts with clearing number that starts with 8
        # has five clearing number digits. Only the four first should
        # be considered when validating though.
        # FIXME: Analyse and address this better.
        return cleaned[:5], cleaned[5:]
    return cleaned[:4], cleaned[4:]
