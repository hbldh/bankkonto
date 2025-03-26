"""
:mod:`test_split_and_clean`
=======================

.. moduleauthor:: hbldh <henrik.blidh@nedomkull.com>
Created on 2017-02-15, 15:07

"""

import pytest

from bankkonto import clean_and_split


@pytest.mark.parametrize(
    "raw, cn, bn",
    [
        ("8156-6 111.222.333-2", "81566", "1112223332"),
        ("8156 111.222.333-2", "81561", "112223332"),
        ("9022.43.244.21", "9022", "4324421"),
    ],
)
def test_split_and_clean(raw: str, cn: str, bn: str) -> None:
    assert clean_and_split(raw) == (cn, bn)
