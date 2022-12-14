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


class RadioButtonPageLocators:
    YES_RADIO = (By.CSS_SELECTOR, "label[class*='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, "label[class*='custom-control'][for='impressiveRadio']")
    NO_RADIO = (By.CSS_SELECTOR, "label[class*='custom-control'][for='noRadio']")
    RADIO_BUTTONS = (By.CSS_SELECTOR, "label[class*='custom-control']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablePageLocators:
    # add new person
    ADD_BTN_PERSON = (By.XPATH, "//button[@id='addNewRecordButton']")
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    AGE = (By.XPATH, "//input[@id='age']")
    SALARY = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT = (By.XPATH, "//input[@id='department']")
    SUBMIT_BTN = (By.XPATH, "//button[@id='submit']")

    # search box
    SEARCH_FIELD = (By.XPATH, "//input[@id='searchBox']")

    # check new person
    PERSON_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")

    # edit person
    EDIT_RECORD_BUTTONT = (By.XPATH, "//span[@title='Edit']")

    # delete person
    DELETE_RECORD_BUTTON = (By.XPATH, "//span[@title='Delete']")
    DELETE_TEXT = (By.CSS_SELECTOR, "div[class ='rt-noData']")

    # change count row
    CHANGE_VALUE = (By.CSS_SELECTOR, "select[aria-label ='rows per page']")


class ButtonPageLocators:
    DOUBLE_CLICK_BTN = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BTN = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME_BTN = (By.XPATH, "//button[text()='Click Me']")

    DOUBLE_CLICK_BTN_TEXT = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_BTN_TEXT = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    CLICK_ME_BTN_TEXT = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")


class LinksPageLocators:
    SIMPLE_LINK = (By.XPATH, "//a[@id='simpleLink']")
    DYNAMIC_LINK = (By.XPATH, "//a[@id='dynamicLink']")
    CREATED_LINK = (By.XPATH, "//a[@id='created']")
    NO_CONTENT_LINK = (By.XPATH, "//a[@id='no-content']")
    MOVED_LINK = (By.XPATH, "//a[@id='moved']")
    BAD_REQUEST_LINK = (By.XPATH, "//a[@id='bad-request']")
    UNAUTHORIZED_LINK = (By.XPATH, "//a[@id='unauthorized']")
    FORBIDDEN_LINK = (By.XPATH, "//a[@id='forbidden']")
    INVALID_URL_LINK = (By.XPATH, "//a[@id='invalid-url']")


class DownloadUploadPageLocators:
    DOWNLOAD_FILE_BTN = (By.XPATH, "//a[@id='downloadButton']")

    UPLOAD_FILE_BTN = (By.XPATH, "//input[@type='file']")
    UPLOADED_FILE_NAME_TEXT = (By.XPATH, "//p[@id='uploadedFilePath']")


class DynamicPropertiesPageLocators:
    ENABLE_BTN = (By.XPATH, "//button[@id='enableAfter']")
    COLOR_TEXT_BTN = (By.XPATH, "//button[@id='colorChange']")
    VISIBLE_AFTER_FIVE_SEC_BTN = (By.XPATH, "//button[@id='visibleAfter']")
