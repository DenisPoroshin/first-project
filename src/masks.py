import logging

logging.basicConfig(
    filename="../logs/masks.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    level=logging.DEBUG,
)

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""
    logger.info(f"Номер карты: {card_number}")
    if len(card_number) == 16 and card_number.isdigit():
        logger.info("Применение маскировки...")
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        logger.error("Некорректный ввод")
        raise ValueError("Некорректный ввод")
    logger.info(f"Результат: {masked_number}")
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера счета"""
    logger.info(f"Номер счета: {account_number}")
    if len(account_number) == 20 and account_number.isdigit():
        logger.info("Применение маскировки...")
        masked_account = f"**{account_number[-4:]}"
    else:
        logger.error("Некорректный ввод")
        raise ValueError("Некорректный ввод")
    logger.info(f"Результат: {masked_account}")
    return masked_account


get_mask_card_number("1234567891234560")
get_mask_account("12345678912345678900")
