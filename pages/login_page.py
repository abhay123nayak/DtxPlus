import time
from locators.login_locators import LoginLocators
from utils.helpers import ElementHelper
from utils.config import Config

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = ElementHelper(driver)
        self.config = Config()

    def load(self):
        base_url = self.config.get('DEFAULT', 'base_url')
        self.driver.get(base_url)

    def login(self, username=None, password=None):
        if not username:
            username = self.config.get('DEFAULT', 'username')
        if not password:
            password = self.config.get('DEFAULT', 'password')

        self.helper.enter_text(LoginLocators.USERNAME_INPUT, username)
        time.sleep(1)
        self.helper.enter_text(LoginLocators.PASSWORD_INPUT, password)
        time.sleep(1)
        self.helper.click(LoginLocators.LOGIN_BUTTON)
        time.sleep(2)

    def get_title_text(self):
        return self.helper.find(LoginLocators.DASHBOARD_TITLE).text
