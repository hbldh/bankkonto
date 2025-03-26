"""
:mod:`exceptions`
=======================

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>
Created on 2017-02-15, 13:56

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import


class BankkontoException(Exception):
    """Base exception class for this module."""

    pass


class BankkontoValidationError(BankkontoException):
    """Validation of bank account number failed."""

    pass


class SwedbankBankkontoValidationError(BankkontoValidationError):
    """Validation of Swedbank bank account number failed."""

    pass
