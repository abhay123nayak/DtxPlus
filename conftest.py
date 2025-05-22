import pytest
from utils.driver_factory import DriverFactory
from utils.config import Config

@pytest.fixture(scope="function")
def setup():
    config = Config()
    browser = config.get('DEFAULT', 'browser')
    base_url = config.get('DEFAULT', 'base_url')

    driver = DriverFactory.get_driver(browser)
    driver.get(base_url)

    yield driver
    driver.quit()
