from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # Form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # Created form fields
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "p[id='name']")
    CREATED_EMAIL = (By.CSS_SELECTOR, "p[id='email']")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p[id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p[id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonLocators:
    YES_RADIO = (By.CSS_SELECTOR, "label[class*='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, "label[class*='custom-control'][for='impressiveRadio']")
    NO_RADIO = (By.CSS_SELECTOR, "label[class*='custom-control'][for='noRadio']")
    RADIO_BUTTONS = (By.CSS_SELECTOR, "label[class*='custom-control']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTableLocators:
    # add new person
    ADD_BTN_PERSON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    AGE = (By.XPATH, "//input[@id='age']")
    SALARY = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT = (By.XPATH, "//input[@id='department']")
    SUBMIT_BTN = (By.XPATH, "//button[@id='submit']")

    # check new person
    PERSON_LIST = (By.CSS_SELECTOR, "div[class='rt-tbody'] .rt-tr-group")

