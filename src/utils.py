import json
import logging

logging.basicConfig(
    filename="../logs/utils.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)


def input_transaction(input_list):
    """Функция возвращает список словарей с данными о финансовых транзакциях
    из json-файла."""
    logger.info('Запуск функции "reading_json_file"')
    try:
        with open(input_list, "r", encoding="utf-8") as f:
            logger.info("Открытие файла...")
            transaction = json.load(f)
            logger.info("Файл в формате списка")
        return transaction
    except json.JSONDecodeError:
        logger.error("Файл не преобразовался")
        return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []
    except TypeError:
        logger.error("Файл не в формате списка")
        return []


input_transaction("")
