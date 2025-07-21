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
