import pytest
import allure
from selenium import webdriver

from locators.login_locators import LoginLocators
from pages.login_page import LoginPage
import utils.config as config

@allure.feature("Login")
class TestLogin:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.story("Valid Login")
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login()  # uses default credentials dtxplus/dtxplus
        # Check redirect to dashboard (url contains "dashboard")
        title_text = login_page.get_title_text()
        assert "Patients" in title_text, f"Dashboard title does not contain 'Patients'. Found: '{title_text}'"
