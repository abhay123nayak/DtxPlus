from locators.dashboard_locators import DashboardLocators
from utils.helpers import ElementHelper

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = ElementHelper(driver)

    def get_table_headers(self):
        header_elements = self.helper.find_all(DashboardLocators.TABLE_HEADER)
        return [header.text.strip() for header in header_elements]
