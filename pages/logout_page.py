import time
from utils.helpers import ElementHelper
from locators.logout_locators import LogoutLocators

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = ElementHelper(driver)

    def logout(self):
        self.helper._wait_for(seconds=3)
        self.helper.click(LogoutLocators.LOGOUT_BUTTON)
        self.helper._wait_for(seconds=3)

    def is_logged_out(self):
        return self.helper.is_visible(LogoutLocators.LOGIN_FORM)
