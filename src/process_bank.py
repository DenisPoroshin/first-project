import re
from collections import Counter


def process_bank_search(data: list[dict], search_str: str) -> list[dict]:
    """Функция, которая будет принимать список словарей
    с данными о банковских операциях и строку поиска. Возвращает список словарей,
    у которых в описании есть данная строка."""

    if not data:
        raise ValueError("Список словарей пуст")
    else:
        result = []
        pattern = re.compile(search_str, re.IGNORECASE)

        for operation in data:
            if pattern.search(operation["description"]):
                result.append(operation)
        return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """ Функция, которая будет принимать список словарей
    с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории. """

    if not data:
        raise ValueError("Список словарей пуст")
    elif not categories:
        raise ValueError("Список категорий пуст")
    else:
        category_counts = Counter()
        for operation in data:
            for value in operation.values():
                if value in categories:
                    category_counts[value] += 1
        return category_counts
