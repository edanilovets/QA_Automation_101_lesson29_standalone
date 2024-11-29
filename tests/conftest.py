import allure
import pytest
from selenium.webdriver import Chrome, ChromeOptions, Firefox, FirefoxOptions, Remote
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.main_page import MainPage
from src.utils.settings_reader import SettingsReader


@pytest.fixture(scope="function")
def guest_login_logout(driver: WebDriver, auto_config: dict):
    main_page = MainPage(driver, auto_config)
    main_page.open()
    main_page.click_guest_login()
    yield
    main_page.logout()
