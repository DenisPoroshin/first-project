import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def transaction_amount(transaction):
    """Функция возвращает сумму транзакций в рублях. Если транзакция в USD или EUR конвертирует в рубли."""
    for i in transaction:
        if i == {}:
            return "Нет транзакции!"
        elif i["operationAmount"]["currency"]["code"] == "RUB":
            return i["operationAmount"]["amount"]
        elif i["operationAmount"]["currency"]["code"] != "RUB":
            value = float(i["operationAmount"]["amount"])
            payload = {}
            headers = {"apikey": f"{API_KEY}"}
            if value == "EUR":
                response = requests.get(
                    f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={value}",
                    headers=headers,
                    data=payload,
                )
            elif value == "USD":
                response = requests.get(
                    f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={value}",
                    headers=headers,
                    data=payload,
                )
            else:
                response = requests.get("https://api.apilayer.com/exchangerates_data/convert")
            status_code = response.status_code
            if status_code == 200:
                convert_amount = response.json()
                result = convert_amount["result"]
                return result
            elif status_code == 400:
                return "Запрос содержит синтаксическую ошибку или неверные параметры."
            elif status_code == 500:
                return "Ошибка на сервере"
    return None
