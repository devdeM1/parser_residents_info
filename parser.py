import time

from driver import get_driver
from actions import click_advanced_search, select_minsk, click_search_button
import logging

URL = 'https://www.park.by/residents/'

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def parse_results(driver):
    logging.info("Начинаем парсинг результатов...")


def main():
    setup_logging()

    try:
        with get_driver() as driver:
            driver.get(URL)
            logging.info(f"Открыта страница: {URL}")

            click_advanced_search(driver)
            select_minsk(driver)
            click_search_button(driver)
            logging.info("Фильтры успешно применены")

            parse_results(driver)

    except Exception as e:
        logging.error(f"Критическая ошибка: {e}", exc_info=True)
        if 'driver' in locals():
            driver.save_screenshot('error.png')
            logging.info("Скриншот ошибки сохранён как error.png")


if __name__ == "__main__":
    main()