from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class CarToBeAddedToGarage:
    def __init__(self):
        self.locators = [
            (By.CSS_SELECTOR, ".update-mileage-form_submit"),
            (By.CSS_SELECTOR, ".car_add-expense"),
        ]

    def __call__(self, driver):
        try:
            for locator in self.locators:
                el = WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))
                return el.is_displayed()
        except TimeoutException:
            return False


class CarsNumberToBe:
    def __init__(self, expected_number):
        self.expected_number = expected_number

    def __call__(self, driver: WebDriver):
        cars_elements = driver.find_elements(By.CSS_SELECTOR, ".car-list li")
        return len(cars_elements) == self.expected_number
