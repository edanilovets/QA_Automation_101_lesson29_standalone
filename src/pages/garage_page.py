from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from src.custom_expected_conditions import CarsNumberToBe, CarToBeAddedToGarage
from src.models.car_model import Car
from src.pages.base_page import BasePage
from src.pages.page_elements.left_menu import LeftMenu


class GaragePage(BasePage):
    def __init__(self, driver, qa_auto_config):
        super().__init__(driver, qa_auto_config)
        self.left_menu = LeftMenu(driver, qa_auto_config)

    # Modal window for car adding
    # add_car_btn = AddCarBtn()
    ADD_CAR_BTN = (By.CSS_SELECTOR, "app-garage .btn.btn-primary")
    CAR_BRAND_SELECTOR = (By.ID, "addCarBrand")
    CAR_MODEL_SELECTOR = (By.ID, "addCarModel")
    CAR_MILEAGE_INPUT = (By.ID, "addCarMileage")
    CAR_MILEAGE_SELECTOR = (By.ID, "addCarMileage1")
    ADD_BTN = (By.CSS_SELECTOR, ".modal-footer .btn.btn-primary")

    def open(self):
        url = "/panel/garage"
        self.driver.get(f"{self.base_url}{url}")

    def add_car(self, car: Car, wait_time: int = 5):
        """Adding car to the garage"""
        self.actions.click(self.ADD_CAR_BTN)
        brand_el = Select(self.actions.find(self.CAR_BRAND_SELECTOR))
        WebDriverWait(self.driver, wait_time).until(EC.text_to_be_present_in_element(self.CAR_BRAND_SELECTOR, car.brand))
        brand_el.select_by_visible_text(car.brand)
        model_el = Select(self.actions.find(self.CAR_MODEL_SELECTOR))
        WebDriverWait(self.driver, wait_time).until(EC.text_to_be_present_in_element(self.CAR_MODEL_SELECTOR, car.model))
        model_el.select_by_visible_text(car.model)
        self.actions.fill(self.CAR_MILEAGE_INPUT, car.mileage)
        self.actions.click(self.ADD_BTN)
        WebDriverWait(self.driver, wait_time).until(CarToBeAddedToGarage())

    def wait_for_number_of_cars_to_be(self, num: int = 1, wait_time: int = 5):
        WebDriverWait(self.driver, wait_time).until(CarsNumberToBe(num))

    def get_car_from_garage_by_index(self, index: int = 1) -> Car:
        car_item_el = self.actions.find((By.CSS_SELECTOR, f".car-list li:nth-child({index})"))
        model, brand = car_item_el.find_element(By.CSS_SELECTOR, ".car_name").text.split()
        mileage = car_item_el.find_element(By.CSS_SELECTOR, ".update-mileage-form_input").get_attribute("valueAsNumber")
        return Car(model, brand, float(mileage))

    def assert_that_car_was_added(self, car: Car, index: int = 1):
        actual_car = self.get_car_from_garage_by_index(index)
        assert_that(actual_car).is_equal_to(car)
