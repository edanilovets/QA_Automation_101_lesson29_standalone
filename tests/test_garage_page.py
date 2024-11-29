import allure
import pytest

from src.models.car_model import Car
from src.pages.garage_page import GaragePage
from tests.base_test import BaseTest


@allure.epic("Car Garage Epic")
@allure.feature("Instructions Feature")
class TestGaragePage(BaseTest):
    """Test Garage page"""

    @allure.story("Add car")
    @allure.tag("Car")
    @allure.title("Add car to the garage")
    @pytest.mark.smoke
    def test_add_car(self, driver, auto_config, login_as_guest):
        """Test adding a car to the garage. Verify that the car was added."""
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
