"""
:mod:`test_clearing`
=======================

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>
Created on 2017-02-15, 15:07

"""
from typing import Tuple

import pytest

from bankkonto.clearing import get_bank_from_clearing_number, get_clearing_ranges_for_bank
from bankkonto.exceptions import BankkontoException


@pytest.mark.parametrize(
    "nbr,expected",
    [
        ("9185", "Danske Bank"),
        ("3300", "Nordea"),
        ("9069", "Länsförsäkringar Bank"),
        ("7000", "Swedbank"),
        ("8000", "Swedbank"),
        ("9300", "Swedbank"),
        ("9330", "Swedbank"),
    ],
)
def test_clearing_number_2_bank_name(nbr: str | int, expected: str) -> None:
    assert get_bank_from_clearing_number(nbr) == expected


@pytest.mark.parametrize(
    "nbr,expected",
    [
        ("9999", "Danske Bank"),
        ("2200", "Nordea"),
        ("32200", "Nordea"),
    ],
)
def test_clearing_number_2_bank_name_failures(nbr: str, expected: str) -> None:
    with pytest.raises(BankkontoException):
        assert get_bank_from_clearing_number(nbr) == expected


@pytest.mark.parametrize(
    "bank,expected",
    [
        ("Danske Bank", ((1200, 1399), (2400, 2499), (9180, 9189))),
        ("Länsförsäkringar Bank", ((3400, 3409), (9020, 9029), (9060, 9069))),
    ],
)
def test_bank_name_2_clearing_number_range(bank: str, expected: tuple[tuple[int, ...]]) -> None:
    assert get_clearing_ranges_for_bank(bank) == expected


@pytest.mark.parametrize(
    "bank,expected",
    [
        ("XDanske BankX", ((1200, 1399), (2400, 2499), (9180, 9189))),
        ("XLänsförsäkringar BankX", ((3400, 3409), (9020, 9029), (9060, 9069))),
    ],
)
def test_bank_name_2_clearing_number_range_failures(bank: str, expected: Tuple[Tuple[int, ...]]) -> None:
    with pytest.raises(BankkontoException):
        assert get_clearing_ranges_for_bank(bank) == expected
