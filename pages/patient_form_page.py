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
        time.sleep(4)
        self.helper.enter_text(PatientFormLocators.MRN, data["mrn"])
        time.sleep(4)
        self.helper.enter_text(PatientFormLocators.FIRST_NAME, data["first_name"])
        time.sleep(4)
        self.helper.enter_text(PatientFormLocators.LAST_NAME, data["last_name"])
        time.sleep(4)
        self.helper.enter_text(PatientFormLocators.DOB, data["dob"])
        time.sleep(4)
        self.helper.enter_text(PatientFormLocators.DISCHARGE_DATE, data["discharge"])
        time.sleep(4)
        self.helper.enter_text(PatientFormLocators.PHONE, data["phone"])
        time.sleep(4)
        self.helper.select_by_visible_text(PatientFormLocators.LANGUAGE_DROPDOWN, data["language"])
        time.sleep(4)
        self.helper.select_by_visible_text(PatientFormLocators.TIMEZONE_DROPDOWN, data["timezone"])
        time.sleep(4)

    def submit(self):
        self.helper.click(PatientFormLocators.SUBMIT_BUTTON)
