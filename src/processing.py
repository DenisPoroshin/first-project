def filter_by_state(list_of_dict: list, state="EXECUTED") -> list:
    """Функция, которая фильтрует список по указанному значению"""
    filtered_list = []
    for dict_item in list_of_dict:
        if dict_item.get("state") == state:
            filtered_list.append(dict_item)
        else:
            continue

    return filtered_list



