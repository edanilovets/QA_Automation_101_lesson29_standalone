from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from src.custom_expected_conditions import CarsNumberToBe, CarToBeAddedToGarage
from src.models.car_model import Car
from src.pages.base_page import BasePage
from src.pages.page_elements.left_menu import LeftMenu


class InstructionsPage(BasePage):
    def __init__(self, driver, qa_auto_config):
        super().__init__(driver, qa_auto_config)
        self.left_menu = LeftMenu(driver, qa_auto_config)

    def open(self):
        url = "/panel/instructions"
        self.driver.get(f"{self.base_url}{url}")

    def click_download(self, title: str):
        pass