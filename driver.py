from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@contextmanager
def get_driver():
    driver = None
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        yield driver
    except Exception as e:
        print(f"Ошибка при инициализации драйвера: {e}")
        raise
    finally:
        if driver:
            driver.quit()