from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class ElementActions:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator: tuple[By, str], timeout: int = 5):
        try:
            element = WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise NoSuchElementException(f"No element found with locator {locator[1]}")

    def click(self, locator: tuple[By, str], timeout: int = 5):
        self.find(locator, timeout).click()

    def fill(self, locator: tuple[By, str], text: str, timeout: int = 5):
        el = self.find(locator, timeout)
        el.clear()
        el.send_keys(text)