import pytest
import allure
from selenium import webdriver

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@allure.feature("Dashboard")
class TestDashboard:

    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.story("Verify dynamic patient table headers")
    def test_patient_table_headers(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login()

        dashboard_page = DashboardPage(driver)
        actual_headers = dashboard_page.get_table_headers()

        expected_headers = [
            "MRN", "First Name", "Last Name", "Date of Birth",
            "Discharge Date & Time", "Phone Number", "Date Added",
            "Language", "Timezone"
        ]

        assert actual_headers == expected_headers, (
            f"Expected headers: {expected_headers}, but found: {actual_headers}"
        )
        print("test case passed for table header matched")

