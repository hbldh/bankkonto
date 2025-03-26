"""
:mod:`account`
=======================

List of bank account number formats from `Bankgirot
<https://www.bankgirot.se/globalassets/dokument/anvandarmanualer/bankernaskontonummeruppbyggnad_anvandarmanual_sv.pdf>
`_.

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>
Created on 2017-02-15, 11:41

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import re
from typing import Literal

from bankkonto.exceptions import BankkontoValidationError, SwedbankBankkontoValidationError

TYPE_1_ACCOUNT_NUMBERS = """
Svea Bank AB 9660-9669 00000xxxxxxC 2
Avanza Bank AB 9550-9569 00000xxxxxxC 2
BlueStep Finans AB 9680-9689 00000xxxxxxC 1
BNP Paribas SA., Sverige filial 9470-9479 00000xxxxxxC 2
Citibank 9040-9049 00000xxxxxxC 2
Danske Bank 1200-1399 00000xxxxxxC 1
Danske Bank 2400-2499 00000xxxxxxC 1
DNB Bank 9190-9199 00000xxxxxxC 2
DNB Bank 9260-9269 00000xxxxxxC 2
Ekobanken 9700-9709 00000xxxxxxC 2
Erik Penser AB 9590-9599 00000xxxxxxC 2
Forex Bank 9400-9449 00000xxxxxxC 1
ICA Banken AB 9270-9279 00000xxxxxxC 1
IKANO Bank 9170-9179 00000xxxxxxC 1
JAK Medlemsbank 9670-9679 00000xxxxxxC 2
Klarna Bank 9780-9789 00000xxxxxxC 2
Landshypotek AB 9390-9399 00000xxxxxxC 2
Lån & Spar Bank Sverige 9630-9639 00000xxxxxxC 1
Länsförsäkringar Bank 3400-3409 00000xxxxxxC 1
Länsförsäkringar Bank 9020-9029 00000xxxxxxC 2
Länsförsäkringar Bank 9060-9069 00000xxxxxxC 1
Marginalen Bank 9230-9239 00000xxxxxxC 1
MedMera Bank AB 9650-9659 00000xxxxxxC 2
Nordax Bank AB 9640-9649 00000xxxxxxC 2
Nordea 1100-1199 00000xxxxxxC 1
Nordea 1400-2099 00000xxxxxxC 1
Nordea 3000-3299 00000xxxxxxC 1
Nordea 3301-3399 00000xxxxxxC 1
Nordea 3410-3781 00000xxxxxxC 1
Nordea 3783-3999 00000xxxxxxC 1
Nordea 4000-4999 00000xxxxxxC 2
Nordnet Bank 9100-9109 00000xxxxxxC 2
Resurs Bank 9280-9289 00000xxxxxxC 1
Riksgälden 9880-9889 00000xxxxxxC 2
Santander Consumer Bank AS 9460-9469 00000xxxxxxC 1
SBAB 9250-9259 00000xxxxxxC 1
SEB 5000-5999 00000xxxxxxC 1
SEB 9120-9124 00000xxxxxxC 1
SEB 9130-9149 00000xxxxxxC 1
Skandiabanken 9150-9169 00000xxxxxxC 2
Swedbank 7000-7999 00000xxxxxxC 1
Ålandsbanken Sverige AB 2300-2399 00000xxxxxxC 2
"""

TYPE_2_ACCOUNT_NUMBERS = """
Danske Bank 9180-9189 00xxxxxxxxxC 1
Handelsbanken 6000-6999 000xxxxxxxxC 2
Nordea/Plusgirot 9500-9549 00xxxxxxxxxC 3
Nordea/Plusgirot 9960-9969 00xxxxxxxxxC 3
Nordea - personkonto 3300 00xxxxxxxxxC 1
Nordea - personkonto 3782 00xxxxxxxxxC 1
Riksgälden 9890-9899 00xxxxxxxxxC 1
Sparbanken Syd 9570-9579 00xxxxxxxxxC 1
Swedbank 8000-8999 00xxxxxxxxxC 3
Swedbank 9300-9329 00xxxxxxxxxC 1
Swedbank 9330-9349 00xxxxxxxxxC 1
"""


_type_1 = [
    (
        _parse_result[0],
        int(_parse_result[1]),
        int(_parse_result[2]) if _parse_result[2] else int(_parse_result[1]),
        _parse_result[3],
        int(_parse_result[4]),
    )
    for _parse_result in re.findall("(.+)\\s([\\d]+)-*(\\d*)\\s(0+x+C)\\s(\\d+)", TYPE_1_ACCOUNT_NUMBERS.strip())
]
_type_1.sort(key=lambda x: x[1])

_type_2 = [
    (
        _parse_result[0],
        int(_parse_result[1]),
        int(_parse_result[2]) if _parse_result[2] else int(_parse_result[1]),
        _parse_result[3],
        int(_parse_result[4]),
    )
    for _parse_result in re.findall("(.+)\\s([\\d]+)-*(\\d*)\\s(0+x+C)\\s(\\d+)", TYPE_2_ACCOUNT_NUMBERS.strip())
]
_type_2.sort(key=lambda x: x[1])


def validate(clearing_number: str, bank_account_number: str) -> Literal[True]:  # noqa: C901

    clearing_number = re.sub("\\D", "", str(clearing_number))
    bank_account_number = re.sub("\\D", "", str(bank_account_number))

    bank_name, type_, nbr_format, footnote = get_account_number_format_based_on_clearing_number(clearing_number)

    if len(nbr_format.strip("0")) != len(bank_account_number):
        raise BankkontoValidationError(
            "Bank account number for {0} must be {1} digits.".format(bank_name, len(nbr_format.strip("0")))
        )

    if type_ == 1:
        if footnote == 1:
            if not _module_11(clearing_number[1:], bank_account_number):
                raise BankkontoValidationError(
                    "Bank account number {0} for {1} has invalid control digit: {2}".format(
                        bank_account_number, bank_name, bank_account_number[-1]
                    )
                )
        elif footnote == 2:
            if not _module_11(clearing_number, bank_account_number):
                raise BankkontoValidationError(
                    "Bank account number {0} for {1} has invalid control digit: {2}".format(
                        bank_account_number, bank_name, bank_account_number[-1]
                    )
                )
        else:
            raise BankkontoValidationError("Unknown Type 1 footnote value: {0}.".format(footnote))
    elif type_ == 2:
        if footnote == 1:
            if not _module_10(bank_account_number):
                raise BankkontoValidationError(
                    "Bank account number {0} for {1} has invalid control digit: {2}".format(
                        bank_account_number, bank_name, bank_account_number[-1]
                    )
                )
        elif footnote == 2:
            if not _module_11("", bank_account_number):
                raise BankkontoValidationError(
                    "Bank account number {0} for {1} has invalid control digit: {2}".format(
                        bank_account_number, bank_name, bank_account_number[-1]
                    )
                )
        elif footnote == 3:
            if not _module_10(bank_account_number):
                # The account number consists of 10 digits. Checksum calculation uses the last ten digits using
                # the modulus 10 check, according format for account number (clearing number not
                # included). However in rare occasions some of Swedbank’s accounts cannot be validated by
                # a checksum calculation.
                message = "Bank account number {0} for {1} has invalid control digit: {2}".format(
                    bank_account_number, bank_name, bank_account_number[-1]
                )
                if bank_name == "Swedbank":
                    raise SwedbankBankkontoValidationError(message)
                raise BankkontoValidationError(message)
        else:
            raise BankkontoValidationError("Unknown Type 2 footnote value: {0}.".format(footnote))
    else:
        raise BankkontoValidationError("Unknown account type: {0}.".format(type_))

    return True


def get_account_number_format_based_on_clearing_number(clearing_number: str) -> tuple[str, int, str, int]:
    if clearing_number[0] == "8":
        # Swedbank account. Clearing number has five digits.
        # Disregard the last one for validation purposes.
        if len(clearing_number) != 5:
            raise BankkontoValidationError("Clearing number for Swedbank accounts must be 5 digits.")
        clearing_number = clearing_number[:-1]
    else:
        if len(clearing_number) != 4:
            raise BankkontoValidationError("Clearing number must be 4 digits.")

    clearing_number_int = int(clearing_number)
    if clearing_number_int < 1000 or clearing_number_int > 9999:
        raise BankkontoValidationError("Clearing number must be in range 1000 - 9999.")

    res = list(filter(lambda x: x[1] <= clearing_number_int <= x[2], _type_1))
    if res:
        return res[0][0], 1, res[0][3], res[0][4]

    res = list(filter(lambda x: x[1] <= clearing_number_int <= x[2], _type_2))
    if res:
        return res[0][0], 2, res[0][3], res[0][4]

    raise BankkontoValidationError(
        "Clearing number {0} does not correspond to any Swedish bank.".format(clearing_number_int)
    )


def is_swedbank(clearing_number: str) -> bool:
    bank_name, _, _, _ = get_account_number_format_based_on_clearing_number(clearing_number)
    return bank_name == "Swedbank"


def expected_account_length(clearing_number: str) -> int:
    _, _, nbr_format, _ = get_account_number_format_based_on_clearing_number(clearing_number)

    return len(nbr_format.strip("0"))


def _module_11(clearing_number: str, bank_account_number: str) -> int:
    weights = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    value = sum([weights[i] * int(c) for i, c in enumerate((str(clearing_number) + str(bank_account_number))[::-1])])
    return (value % 11) == 0


def _module_10(bank_account_number: str) -> int:
    values = [(2 if i % 2 else 1) * int(c) for i, c in enumerate((str(bank_account_number))[::-1])]
    value = sum([(v - 9) if (v > 9) else v for v in values])
    return (value % 10) == 0
