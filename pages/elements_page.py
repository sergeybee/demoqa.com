from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('dflsdf')
        self.element_is_visible(self.locators.EMAIL).send_keys('sdf@kdf.ru')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('kfkfkf')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('ieirworw')
        self.element_is_visible(self.locators.SUBMIT).click()

    def check_field_form(self):
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_adress = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_adress = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_adress, permanent_adress
