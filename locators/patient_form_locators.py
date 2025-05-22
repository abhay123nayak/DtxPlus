from selenium.webdriver.common.by import By

class PatientFormLocators:
    Add_patients_xpath = (By.ID,"add-patient-btn")
    FORM = (By.ID, "patient-form")
    MRN = (By.ID, "mrn")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    DOB = (By.ID, "dob")
    DISCHARGE_DATE = (By.ID, "discharge")
    PHONE = (By.ID, "phone")
    LANGUAGE_DROPDOWN = (By.ID, "language")
    TIMEZONE_DROPDOWN = (By.ID, "timezone")
    SUBMIT_BUTTON = (By.XPATH, "//form[@id='patient-form']//button[@type='submit']")
