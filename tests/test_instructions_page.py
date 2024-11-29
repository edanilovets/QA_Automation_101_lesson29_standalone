import allure
import pytest
from assertpy import assert_that

from src.models.car_model import Car
from src.pages.instructions_page import InstructionsPage
from src.utils.files_utils import FileUtils
from tests.base_test import BaseTest


@allure.epic("Car Garage Epic")
@allure.feature("Instructions Feature")
class TestInstructionsPage(BaseTest):
    """Test Instructions page"""

    @allure.story("Download instruction")
    @allure.issue("https://eugenedanilovets.atlassian.net/browse/QA-4", "QA-4 Instruction is not downloaded")
    def test_instruction_download(self, driver, auto_config, guest_login_logout):
        instructions_page = InstructionsPage(driver, auto_config)
        instructions_page.open()
        car = Car(brand="Audi", model="TT")
        instruction_title = "Front windshield wipers on Audi TT"
        # Click download
        # instructions_page.click_download(instruction_title)
        with allure.step("Assert that instruction is downloaded"):
            is_downloaded = FileUtils.wait_for_file_download(f"{instruction_title}.pdf")
            assert_that(is_downloaded).is_true()
