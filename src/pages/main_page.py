from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class MainPage(BasePage):
    GUEST_LOGIN_LINK = (By.CSS_SELECTOR, "button.header-link.-guest")

    def open(self):
        self.driver.get(self.base_url)

    def click_guest_login(self):
        self.actions.click(self.GUEST_LOGIN_LINK)
