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
    if bank_account_number.startswith('8'):
        # Swedbank accounts with clearing 8XXX sometimes has an
        # additional "-X" appended to the clearing number. This
        # value is not to be considered when validating.
        # FIXME: Analyse and address this better.
        if bank_account_number[4] == '-':
            bank_account_number = bank_account_number[:4] + bank_account_number[6:]
    cleaned = re.sub('\D', '', bank_account_number)
    return cleaned[:4], cleaned[4:]
