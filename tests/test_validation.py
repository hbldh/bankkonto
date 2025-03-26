"""
:mod:`test_validation`
=======================

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>
Created on 2017-02-15, 15:07

"""

import pytest

from bankkonto import validate, BankkontoValidationError


@pytest.mark.parametrize(
    "clearing_number,bank_account_number",
    [
        ("1234", "5612541"),
        ("3300", "8012016286"),
        ("6001", "801230659"),
        ("9570", "2600000000"),
        ("9890", "2600000000"),
        ("3782", "2600000000"),
        ("9590", "2000000"),
        ("9598", "2400000"),
    ],
)
def test_validation_ok(clearing_number: str, bank_account_number: str) -> None:
    assert validate(clearing_number, bank_account_number)


@pytest.mark.parametrize(
    "clearing_number,bank_account_number",
    [
        ("9022", "8456424"),
        ("19022", "8456424"),
        ("9022", "84564244343243"),
        ("9680", "1234567"),
        ("0123", "1234567"),
        ("3300", "8012346589"),
        ("6001", "801230658"),
        ("8001", "8012306581"),
        ("9999", "8012306581"),
    ],
)
def test_validation_fails(clearing_number: str, bank_account_number: str) -> None:
    with pytest.raises(BankkontoValidationError):
        assert validate(clearing_number, bank_account_number)
