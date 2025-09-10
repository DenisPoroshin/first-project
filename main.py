from src.utils import reading_json_file
from src.transactions import reading_operations_from_csv, reading_operations_from_excel
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.process_bank import process_bank_search
from src.masks import get_mask_account


def main():
    transactions = []
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    user_choice = input().strip()

    items = {
        "1": ("JSON", "../data/operations.json", reading_json_file),
        "2": ("CSV", "../data/transactions.csv", reading_operations_from_csv),
        "3": ("XLSX", "../data/transactions_excel.xlsx", reading_operations_from_excel),
    }

    if user_choice in items:
        file_format, file, func = items[user_choice]
        print(f"Для обработки выбран {file_format} файл.")
        transactions = func(file)
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

    # Фильтр по статусу
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
        status_choice = input().strip().upper()
        if status_choice in valid_statuses:
            print(f'Операции отфильтрованы по статусу "{status_choice}"')
            state = status_choice
            break
        else:
            print(f'Статус операции "{status_choice}" недоступен.')

    transactions = filter_by_state(transactions, state=state)

    # Сортировка по запросу
    print("Отсортировать операции по дате? Да/Нет")
    sorting = input().lower() == "да"
    print("Отсортировать по возрастанию или по убыванию?")
    ascending = input().lower() == "по возрастанию"
    print("Выводить только рублевые транзакции? Да/Нет")
    rub_filter = input().lower() == "да"
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    keyword_filter = input().lower() == "да"
    print("Программа: Распечатываю итоговый список транзакций...")

    if sorting:
        transactions = sort_by_date(transactions, ascending)
    if rub_filter:
        transactions = filter_by_currency(transactions, "RUB")
    if keyword_filter:
        print("Введите слово для фильтрации:")
        keyword = input().lower()
        transactions = process_bank_search(transactions, keyword)
    else:
        transactions = transactions

    filtered_transactions = []

    for transaction in transactions:
        if transaction.get("from"):
            curr_code_2 = transaction["from"]
            masked_code_2 = get_mask_account(curr_code_2)
            transaction["from"] = masked_code_2

        if transaction.get("to"):
            curr_code_1 = transaction["to"]
            masked_code_1 = get_mask_account(curr_code_1)
            transaction["to"] = masked_code_1

        filtered_transactions.append(transaction)

    transactions = filtered_transactions

    print(f"Всего банковских операций в выборке: {len(transactions)}")

    if not transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    print(main())
