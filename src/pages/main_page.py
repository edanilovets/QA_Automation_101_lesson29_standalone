from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class MainPage(BasePage):
    GUEST_LOGIN_LINK = (By.CSS_SELECTOR, "button.header-link.-guest")
    MY_PROFILE = (By.ID, "userNavDropdown")
    LOGOUT_LINK = (By.XPATH, "//button[contains(text(), 'Logout')]")

    def open(self):
        self.driver.get(self.base_url)

    def click_guest_login(self):
        self.actions.click(self.GUEST_LOGIN_LINK)

    def logout(self):
        self.actions.click(self.MY_PROFILE)
        self.actions.click(self.LOGOUT_LINK)
        self.actions.find(self.GUEST_LOGIN_LINK, timeout=10)
