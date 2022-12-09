from selenium.webdriver.common.by import By


class RegistrationFormPageLocators:
    # Registration Form fields
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    USER_EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER = (By.CSS_SELECTOR, "input[name='gender']")
    USER_PHONE_NUMBER = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    SUBJECTS = (By.CSS_SELECTOR, "input[id='subjectsContainer']")
    PICTURE_FILE = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # Created registration students
    MODAL_WINDOW = (By.CSS_SELECTOR, "div[class='modal-content']")
    HEADER_MODAL_WINDOW = (By.CSS_SELECTOR, "div[id='example-modal-sizes-title-lg']")

    CREATED_LIST_DATA = (By.CSS_SELECTOR, "div[class ='modal-body'] table tbody tr")


