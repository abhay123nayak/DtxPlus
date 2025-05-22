from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
class ElementHelper:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=10):
        el = self.find(locator, timeout)
        el.click()

    def enter_text(self, locator, text, timeout=10):
        el = self.find(locator, timeout)
        el.clear()
        el.send_keys(str(text))

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def select_by_visible_text(self, locator, text):
        element = self.find(locator)
        select = Select(element)
        select.select_by_visible_text(text)
