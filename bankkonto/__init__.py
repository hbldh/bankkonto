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

import sys
import re

from .version import __version__, version  # noqa
from .exceptions import BankkontoException, BankkontoValidationError   # noqa
from .account import validate  # noqa


__all__ = [
    '__version__',
    'version',
    'BankkontoException',
    'BankkontoValidationError',
    'validate',
]


def clean_and_split(bank_account_number: str) -> tuple[str, str]:
    cleaned = re.sub('\\D', '', bank_account_number)
    if cleaned.startswith('8'):
        # Swedbank accounts with clearing number that starts with 8
        # has five clearing number digits. Only the four first should
        # be considered when validating though.
        # FIXME: Analyse and address this better.
        return cleaned[:5], cleaned[5:]
    return cleaned[:4], cleaned[4:]


def cli(args: list[str] | None = None) -> None:
    import argparse
    args = args if args else sys.argv[1:]

    parser = argparse.ArgumentParser(description="Validator for Swedish bank accounts")
    parser.add_argument('clearing_number', type=str, required=True, help="Clearing number with 4 or 5 digits")
    parser.add_argument('account_number', type=str, required=True, help="Account number with 7-10 digits")

    arguments = parser.parse_args(args)
    validate(arguments.clearing_number, arguments.account_number)
    print("{0} {1} is a valid Swedish bank account number".format(
        arguments.clearing_number, arguments.account_number))


if __name__ == '__main__':
    cli(sys.argv[1:])
