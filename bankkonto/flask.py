#!/usr/bin/env python
# -*- coding: utf-8 -*-
# type: ignore
"""
WTForms validator
-----------------

:copyright: 2017-02-16 by hbldh <henrik.blidh@swedwise.com>

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import bankkonto

try:
    from wtforms.validators import ValidationError
except:  # noqa
    # Flask-WTF is not installed. To be able to use this properly
    # it needs to be, so we can safely use ValueError instead.
    ValidationError = ValueError


class BankkontoValidator(object):
    """
    Validates that input in this field is a valid Swedish bank account number.
    """
    field_flags = ('', )

    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, form, field):
        cn, bn = bankkonto.clean_and_split(field.data)
        try:
            bankkonto.validate(cn, bn)
        except bankkonto.BankkontoValidationError as e:
            raise ValidationError(str(e))
