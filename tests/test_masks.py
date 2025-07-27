import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("2000792289606361", "2000 79** **** 6361"),
        ("3596837868705199", "3596 83** **** 5199"),
        ("4158300734726758", "4158 30** **** 6758"),
        ("5831982476737658", "5831 98** **** 7658"),
        ("6990922113665229", "6990 92** **** 5229"),
        ("7999414228426353", "7999 41** **** 6353"),
        ("8888888888888888", "8888 88** **** 8888"),
        ("9999999999999999", "9999 99** **** 9999"),
        ("0000000000000000", "0000 00** **** 0000"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_else() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("1234567890")
        get_mask_card_number("")
        get_mask_card_number("incorrect_input!")


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("64686473678894779589", "**9589"),
        ("15968378687051995199", "**5199"),
        ("20007922896063616361", "**6361"),
        ("35968378687051995199", "**5199"),
        ("41583007347267586758", "**6758"),
        ("58319824767376587658", "**7658"),
        ("69909221136652295229", "**5229"),
        ("79994142284263536353", "**6353"),
        ("88888888888888888888", "**8888"),
        ("99999999999999999999", "**9999"),
        ("00000000000000000000", "**0000"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


def test_get_mask_account_else() -> None:
    with pytest.raises(ValueError):
        get_mask_account("1234567890")
        get_mask_account("")
        get_mask_account("incorrect_input!")
