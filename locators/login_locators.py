from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_INPUT = (By.XPATH, "//input[contains(@id,'username')]")
    PASSWORD_INPUT = (By.XPATH, "//input[contains(@id,'password')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Login')]")
    DASHBOARD_TITLE  = (By.XPATH,"//div[@id='dashboard']/h2")