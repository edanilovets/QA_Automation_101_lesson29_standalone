import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ElementActions:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Find {locator}")
    def find(self, locator: tuple[By, str], timeout: int = 5):
        try:
            element = WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise NoSuchElementException(f"No element found with locator {locator[1]}")

    @allure.step("Click {locator}")
    def click(self, locator: tuple[By, str], timeout: int = 5):
        self.find(locator, timeout).click()

    @allure.step("Fill {locator} with text {text}")
    def fill(self, locator: tuple[By, str], text: str, timeout: int = 5):
        el = self.find(locator, timeout)
        el.clear()
        el.send_keys(text)
