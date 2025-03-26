"""
:mod:`clearing`
=======================

List of clearing numbers fetched from `Swedish Bankers'
Association <http://www.swedishbankers.se/fraagor-vi-arbetar-med/clearingnummer/clearingnummer/>`_.

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>
Created on 2017-02-15, 11:13

"""

import re
from typing import Tuple

from .exceptions import BankkontoException

_CLEARING_LIST = """
Sveriges Riksbank 1000-1099
Nordea 1100-1199
Danske Bank 1200-1399
Nordea 1400-2099
Ålandsbanken 2300-2399
Danske Bank 2400-2499
Nordea 3000-3399
Länsförsäkringar Bank 3400-3409
Nordea 3410-4999
SEB 5000-5999
Handelsbanken 6000-6999
Swedbank 7000-8999
Länsförsäkringar Bank 9020-9029
Citibank 9040-9049
Länsförsäkringar Bank 9060-9069
Calyon Bank 9080-9089
Nordnet Bank 9100-9109
SEB 9120-9124
SEB 9130-9149
Skandiabanken 9150-9169
IKANO Banken 9170-9179
Danske Bank 9180-9189
DNB Bank 9190-9199
Marginalen Bank 9230-9239
SBAB Bank 9250-9259
DNB Bank 9260-9269
ICA Banken 9270-9279
Resurs Bank 9280-9289
Swedbank 9300-9349
Pareto Öhman 9380-9389
Landshypotek 9390-9399
Forex Bank 9400-9449
GE Money Bank 9460-9469
BNP Paribas 9470-9479
Parex Bank 9480-9489
Nordea 9500-9549
Avanza Bank 9550-9569
Sparbanken Syd 9570-9579
Exchange Finans Europe 9580-9589
Erik Penser Bankaktiebolag 9590-9599
Volvofinans Bank 9610-9619
Bank of China (Luxembourg) 9620-9629
Lån & Spar Bank 9630-9639
Nordax Finans 9640-9649
MedMera Bank 9650-9659
Svea Bank 9660-9669
JAK Medlemsbank 9670-9679
Bluestep Finans 9680-9689
Folkia 9690-9699
Ekobanken 9700-9709
Aman Bank (ub) 9710-9719
Netfonds Bank (ub) 9720-9729
Klarna Bank 9780-9789
Privatgirot 9860-9869
Nasdaq-OMX 9870-9879
Riksgälden 9880-9899
Nykredit 9950
Teller Branch Norway 9951
Bankernas Automatbolag 9952
Teller Branch Sweden 9953
Kortaccept Nordic AB 9954
Nordea 9960-9969
"""

clearing_nbrs = [
    (_parse_result[0], int(_parse_result[1]), int(_parse_result[2]) if _parse_result[2] else int(_parse_result[1]))
    for _parse_result in re.findall("(.+)\\s([\\d]+)-*(\\d*)", _CLEARING_LIST.strip())
]
clearing_nbrs.sort(key=lambda x: x[1])


def get_bank_from_clearing_number(nbr: str | int) -> str:
    nbr = int(nbr)

    if nbr < 1000 or nbr > 9999:
        raise BankkontoException("Clearing number must be in range 1000 - 9999.")
    res = list(filter(lambda x: nbr >= x[1] and nbr <= x[2], clearing_nbrs))
    if len(res) == 0:
        raise BankkontoException("Clearing number {0} does not correspond to any Swedish bank.")
    else:
        bank = res[0][0]
        assert isinstance(bank, str)
        return bank


def get_clearing_ranges_for_bank(bank: str) -> Tuple[Tuple[int, ...], ...]:
    res = list(filter(lambda x: x[0] == bank, clearing_nbrs))
    if len(res) == 0:
        raise BankkontoException("Incorrect bank name.")
    else:
        return tuple(tuple(x[1:]) for x in res)
