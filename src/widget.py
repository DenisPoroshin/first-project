from src.masks import get_mask_account, get_mask_card_number


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
