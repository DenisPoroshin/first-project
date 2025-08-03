import pytest

from src.decorators import log


@log(filename="mylog.txt")
def my_function_one(a: int, b: int) -> float:
    """Функция сложения"""
    return a + b


def test_my_function_one_success() -> None:
    my_function_one(4, 2)
    with open(file="mylog.txt"):
        assert "my_function completed successfully. Result: 6"


def test_my_function_one_not_arg() -> None:
    my_function_one(
        4,
    )
    with open(file="mylog.txt"):
        assert "Error in my_function: TypeError. Input: (4,), {}"


@log()
def my_function_two(x: int, y: int) -> float:
    """Функция деления"""
    return x / y


def test_my_function_two_success() -> None:
    my_function_two(4, 2)
    assert "my_function completed successfully. Result: 2"


def test_my_function_two_division_by_zero() -> None:
    my_function_two(4, 0)
    assert "Error in my_function: ZeroDivisionError. Input: (4, 0), {}"
