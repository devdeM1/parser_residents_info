from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


ADVANCED_SEARCH_BUTTON = "//a[@class='collapsed gul']"
SEARCH_BUTTON = "//button[@type='submit' and contains(@value, 'Найти')]"
MINSK_ID = "CITY_612"


def click_advanced_search(driver):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ADVANCED_SEARCH_BUTTON))
        )
        button.click()
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Ошибка при нажатии кнопки расширенного поиска: {e}")
        return False


def select_minsk(driver):
    try:
        checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, MINSK_ID))
        )

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
        driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(1)

        if not checkbox.is_selected():
            raise Exception("Не удалось выбрать чекбокс Минска")

        print("Фильтр 'Минск' успешно применен")
        return True

    except Exception as e:
        print(f"Критическая ошибка при выборе города: {e}")
        driver.save_screenshot("minsk_filter_error.png")
        return False

def click_search_button(driver):
    try:
        search_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SEARCH_BUTTON))
        )
        search_btn.click()
        time.sleep(3)
        return True
    except Exception as e:
        print(f"Ошибка при нажатии кнопки 'Найти': {e}")
        return False