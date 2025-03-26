"""
:mod:`test_flask_validator`
=======================

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>
Created on 2017-02-15, 15:07

"""

import pytest

from bankkonto.flask import BankkontoValidator, ValidationError


class FieldMock(object):
    """Simple WTForms Field Mock object."""

    def __init__(self, data):
        self.data = data


@pytest.mark.parametrize(
    "account_nbr",
    [
        "8156-6 111.222.333-2",
        "81566 111.222.333-2",
        "1234 56.125.41",
        "3300 801201-6286",
        "9022.43.244.21",
    ],
)
def test_validator(account_nbr):
    bv = BankkontoValidator()
    assert bv(None, FieldMock(account_nbr)) is None


@pytest.mark.parametrize(
    "account_nbr",
    [
        "90228456424",
        "190228456424",
        "902284564244343243",
        "96801234567",
        "01231234567",
        "33008012346589",
        "6001801230658",
        "80018012306581",
        "99998012306581",
        "8156-6 111.222.333-6",
    ],
)
def test_validator_fails(account_nbr):
    with pytest.raises(ValidationError):
        bv = BankkontoValidator()
        assert bv(None, FieldMock(account_nbr)) is None
