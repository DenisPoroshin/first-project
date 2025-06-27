def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера счета"""
    masked_account = f"**{account_number[-4:]}"
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

    if "Счет" in card_info:
        masked_number = get_mask_account(card_number)
    else:
        masked_number = get_mask_card_number(card_number)

    return f"{card_type} {masked_number}"


# Пример использования функции
# Входной аргумент
input_card_number = "Maestro 1596837868705199"
input_account_number = "Счет 64686473678894779589"


# Вызов функции и вывод результата
print(mask_account_card(input_card_number))
print(mask_account_card(input_account_number))
