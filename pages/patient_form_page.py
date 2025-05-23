import time
from os import times

from selenium.webdriver.common.by import By

from locators.patient_form_locators import PatientFormLocators
from utils.helpers import ElementHelper

class PatientFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.helper = ElementHelper(driver)

    def fill_form(self, data):
        self.helper.click(PatientFormLocators.Add_patients_xpath)
        self.helper._wait_for(seconds=3)
        self.helper.enter_text(PatientFormLocators.MRN, data["mrn"])
        self.helper.enter_text(PatientFormLocators.FIRST_NAME, data["first_name"])
        self.helper.enter_text(PatientFormLocators.LAST_NAME, data["last_name"])
        self.helper._wait_for(seconds=2)
        self.helper.enter_text(PatientFormLocators.DOB, data["dob"])
        self.helper.enter_text(PatientFormLocators.DISCHARGE_DATE, data["discharge"])
        self.helper.enter_text(PatientFormLocators.PHONE, data["phone"])
        self.helper._wait_for(seconds=2)
        self.helper.select_by_visible_text(PatientFormLocators.LANGUAGE_DROPDOWN, data["language"])
        self.helper._wait_for(seconds=2)
        self.helper.select_by_visible_text(PatientFormLocators.TIMEZONE_DROPDOWN, data["timezone"])
        time.sleep(4)

    def submit(self):
        self.helper.click(PatientFormLocators.SUBMIT_BUTTON)
