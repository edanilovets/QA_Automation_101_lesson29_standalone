import allure
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.main_page import MainPage


class BaseTest:

    @allure.step("Login as guest")
    def login_as_guest(self, driver: WebDriver, auto_config: dict):
        main_page = MainPage(driver, auto_config)
        main_page.open()
        main_page.click_guest_login()

    @allure.step("Login as {username}")
    def login(self, username: str, password: str):
        pass
