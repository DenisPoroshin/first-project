from masks import get_mask_card_number, get_mask_account


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

    if card_type.lower() in ["Счет"]:
        masked_number = get_mask_account(card_number)
    else:
        masked_number = get_mask_card_number(card_number)

    return f"{card_type} {masked_number}"



