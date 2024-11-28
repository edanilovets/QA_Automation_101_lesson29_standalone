import allure

from src.models.car_model import Car
from src.pages.garage_page import GaragePage
from tests.base_test import BaseTest


@allure.epic("QA-10 Garage Epic")
@allure.feature("QA-100 Garage Feature")
class TestGaragePage(BaseTest):
    """Test Garage page"""

    @allure.story("QA-102 Add Cars to Garage Story")
    @allure.title("Add car to garage")
    @allure.description("Verify that user can add car to garage")
    @allure.link("https://jira.example.com/browse/QA-102")
    def test_add_car(self, driver, auto_config):
        # Login as guest
        self.login_as_guest(driver, auto_config)
        # Add car
        garage_page = GaragePage(driver, auto_config)
        # garage_page.left_menu.select_menu("Garage")
        cars = [
            Car(brand="Porsche", model="Cayenne", mileage=1000.54),
            Car(brand="Audi", model="Q7", mileage=19999)
        ]
        for car in cars:
            garage_page.add_car(car)

        # Verify added car
        garage_page.wait_for_number_of_cars_to_be(2)
        for index, car in enumerate(cars):
            garage_page.assert_that_car_was_added(car, len(cars) - index)
