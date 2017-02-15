#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:mod:`test_validation`
=======================

.. moduleauthor:: hbldh <henrik.blidh@swedwise.com>
Created on 2017-02-15, 15:07

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import pytest

from bankkonto import validate, BankkontoValidationError


@pytest.mark.parametrize("clearing_number,bank_account_number", [
    ('1234', '5612541'),
])
def test_validation_ok(clearing_number, bank_account_number):
    assert validate(clearing_number, bank_account_number)


@pytest.mark.parametrize("clearing_number,bank_account_number", [
    ('9022', '8456424'),
])
def test_validation_fails(clearing_number, bank_account_number):
    with pytest.raises(BankkontoValidationError):
        assert validate(clearing_number, bank_account_number)
