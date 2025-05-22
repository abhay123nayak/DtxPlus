from selenium.webdriver.common.by import By


class DashboardLocators:
    TABLE_HEADER = (By.XPATH, "//table[@id='patients-table']/thead/tr/th")
