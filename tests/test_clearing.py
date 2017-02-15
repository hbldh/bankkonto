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

from bankkonto.clearing import get_bank_from_clearing_number, get_clearing_ranges_for_bank


@pytest.mark.parametrize("nbr,expected", [
    ('9185', 'Danske Bank'),
    ('3300', 'Nordea'),
    ('9069', 'Länsförsäkringar Bank'),
])
def test_clearing_number_2_bank_name(nbr, expected):
    assert get_bank_from_clearing_number(nbr) == expected


@pytest.mark.parametrize("bank,expected", [
    ('Danske Bank', ((1200, 1399), (2400, 2499), (9180, 9189))),
    ('Länsförsäkringar Bank', ((3400, 3409), (9020, 9029), (9060, 9069))),
])
def test_bank_name_2_clearing_number_range(bank, expected):
    assert get_clearing_ranges_for_bank(bank) == expected
