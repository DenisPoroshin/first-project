def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""
    if len(card_number) == 16 and card_number.isdigit():
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        raise ValueError("Некорректный ввод")
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера счета"""
    if len(account_number) == 20 and account_number.isdigit():
        masked_account = f"**{account_number[-4:]}"
    else:
        raise ValueError("Некорректный ввод")
    return masked_account



def mask_account_card(card_info: str) -> str:
    """Функция для маскировки номера карты или счета."""
    card_type_list = []
    card_number_list = []
    card_info_list = card_info.split()

    for string in card_info_list:
        if string.isalpha():
            card_type_list.append(string)
        elif string.isdigit():
            card_number_list.append(string)

    card_type = " ".join(card_type_list)
    card_number = " ".join(card_number_list)

    if card_type.lower() in ["счет"]:
        masked_number = get_mask_account(card_number)
    else:
        masked_number = get_mask_card_number(card_number)

    return f"{card_type} {masked_number}"


def get_date(date_str: str) -> str:
    """Функция для реформации даты"""
    date_list = date_str.split("-", 2)
    date_list[2] = date_list[2][:2]
    date_list_reverse = ".".join(date_list[::-1])
    return date_list_reverse


def filter_by_state(list_of_dict: list, state="EXECUTED") -> list:
    """Функция, которая фильтрует список по указанному значению"""

    filtered_list = []

    for dict_item in list_of_dict:
        if dict_item.get("state") == state:
            filtered_list.append(dict_item)
        else:
            continue
    return filtered_list


def sort_by_date(list_of_date: list, method_sort=True) -> list:
    """Функция, которая сортирует список по дате"""
    sorted_list_of_date = sorted(list_of_date, key=lambda i: i["date"], reverse=method_sort)
    return sorted_list_of_date


# Пример использования функции
# Входной аргумент
input_card_number = "Maestro 1596837868705199"
input_account_number = "Счет 64686473678894779589"
input_date = "2024-03-11T02:26:18.671407"
input_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

# Вызов функции и вывод результата
print(mask_account_card(input_card_number))
print(mask_account_card(input_account_number))
print(get_date(input_date))
print(filter_by_state(input_list))
print(sort_by_date(input_list))
