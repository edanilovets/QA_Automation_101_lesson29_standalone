import allure
import pytest
from assertpy import assert_that

from src.models.car_model import Car
from src.pages.instructions_page import InstructionsPage
from src.utils.files_utils import FileUtils
from tests.base_test import BaseTest


@allure.feature("QA-100 Garage Feature")
class TestInstructionsPage(BaseTest):
    """Test Instructions page"""

    @allure.story("QA-101 Download Instructions Story")
    def test_instruction_download(self, driver, auto_config):
        # Login as guest
        self.login_as_guest(driver, auto_config)
        instructions_page = InstructionsPage(driver, auto_config)
        instructions_page.open()
        # car = Car(brand="Audi", model="TT")
        instruction_title = "Front windshield wipers on Audi TT"
        file_name = f"{instruction_title}.pdf"
        # instructions_page.click_download(instruction_title)
        with allure.step(f"Wait for file download {file_name}"):
            is_downloaded = FileUtils.wait_for_file_download(file_name)

        with allure.step(f"Verify that file {file_name} was downloaded"):
            assert_that(is_downloaded).is_true()
