import time

import pytest
import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.patient_form_page import PatientFormPage

@allure.feature("Add Patient Form")
class TestPatientForm:

    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.story("Submit valid patient form")
    def test_valid_patient_add(self, driver):
        login = LoginPage(driver)
        login.load()
        login.login()
        form = PatientFormPage(driver)
        patient = {
            "mrn": "MRN1001",
            "first_name": "Alice",
            "last_name": "Smith",
            "dob": "1985-10-10",
            "discharge": "2025-05-23 09:00",
            "phone": "9876543210",
            "language": "English",
            "timezone": "PST"
        }

        form.fill_form(patient)
        form.submit()
        self.helper._wait_for(seconds=10)
