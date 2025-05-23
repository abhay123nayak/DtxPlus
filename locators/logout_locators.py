from selenium.webdriver.common.by import By

class LogoutLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Logout')]")

    LOGIN_FORM = (By.XPATH,"//form[@id='login-form']")
