def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера счета"""
    masked_account = f"**{account_number[-4:]}"
    return masked_account


# Пример использования функции
# Входной аргумент
input_card_number = "7000792289606361"
input_account_number = "73654108430135874305"

# Вызов функции и вывод результата
print(get_mask_card_number(input_card_number))  # выход функции: 7000 79** **** 6361
print(get_mask_account(input_account_number))  # выход функции: **4305
