import pytest
import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

@allure.feature("Logout")
class TestLogout:

    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.story("Valid Logout")
    def test_logout_flow(self, driver):
        login = LoginPage(driver)
        login.load()
        login.login()

        logout = LogoutPage(driver)
        logout.logout()

        assert logout.is_logged_out(), "Logout failed, login button not visible."
