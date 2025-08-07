import pytest

from src.decorators import log


def test_log():
    @log(filename="my_log.txt")
    def summa(x, y):
        return x + y

    result_summa = summa(1, 2)
    assert f"summa ок. Результат: {result_summa}" == "summa ок. Результат: 3"

    @log(filename="my_log.txt")
    def sub(x, y):
        return x - y

    result_sub = sub(2, 1)
    assert f"sub ок. Результат: {result_sub}" == "sub ок. Результат: 1"

    @log(filename="my_log.txt")
    def division(x, y):
        return x / y

    result_division = division(4, 2)
    assert f"division ок. Результат: {result_division}" == "division ок. Результат: 2.0"


@log()
def my_function(x, y):
    return x / y


def test_decorator_cupsys(capsys):
    with pytest.raises(Exception):
        my_func_one = my_function()
        my_func_two = my_function(1, 0)
        captured = my_func_one.readouterr() and my_func_two.readouterr()
        assert captured.out == Exception
