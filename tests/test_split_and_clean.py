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

from bankkonto import clean_and_split
from bankkonto.exceptions import BankkontoException

@pytest.mark.parametrize("raw, cn, bn", [
    ('8156-6 111.222.333-2', '8156', '1112223332'),
    ('8156 111.222.333-2', '8156', '1112223332'),
    ('9022.43.244.21', '9022', '4324421'),
])
def test_split_and_clean(raw, cn, bn):
    assert clean_and_split(raw) == (cn, bn)
