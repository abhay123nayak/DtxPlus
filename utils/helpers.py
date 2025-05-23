from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
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

    @staticmethod
    def _wait_for(seconds):
        """Wait for the given number of seconds (must be provided)."""
        time.sleep(seconds)


    def is_visible(self, locator):
        try:
            return self.find(locator).is_displayed()
        except:
            return False