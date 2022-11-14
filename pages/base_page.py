from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def elemement_is_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, locator, timeout).until(EC.visibility_of_element_located(locator))

    def elemements_are_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, locator, timeout).until(EC.visibility_of_all_elements_located(locator))

    def elemement_is_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, locator, timeout).until(EC.presence_of_element_located(locator))

    def elemements_are_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, locator, timeout).until(EC.presence_of_all_elements_located(locator))

    def elemements_is_not_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, locator, timeout).until(EC.invisibility_of_element_located(locator))

    def elemement_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, locator, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].ScrollIntoView;")
