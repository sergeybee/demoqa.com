import random

from selenium.webdriver.common.by import By


class FormPageLocators:
    # Registration Form fields
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    USER_EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1, 3)}']")
    USER_PHONE_NUMBER = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "div[class='react-datepicker__input-container'] input")
    SUBJECTS = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    UPLOAD_PICTURE_FILE = (By.XPATH, "//input[@type='file']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # Created registration students
    RESULT_FILLS_FORM = (By.XPATH, "//div[@class='table-responsive']//td[2]")


