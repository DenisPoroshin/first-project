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
