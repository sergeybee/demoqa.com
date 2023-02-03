import os
import time

from selenium.webdriver import Keys

from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person, generated_file, generate_subject, generate_state_and_city


class RegistrationStudentForm(BasePage):
    """Форма регистрации студентов"""

    locators = FormPageLocators()

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_PICTURE_FILE).send_keys(path)
        return file_name

    def fills_data_in_the_form_fields(self):
        person_data = next(generated_person())
        file_name, path = generated_file()
        state, city = generate_state_and_city()
        subject = generate_subject()

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person_data.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person_data.last_name)
        self.element_is_visible(self.locators.USER_EMAIL).send_keys(person_data.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.USER_PHONE_NUMBER).send_keys(person_data.phone_number)
        date_birth = self.element_is_visible(self.locators.DATE_OF_BIRTH).get_attribute('value')
        self.element_is_visible(self.locators.SUBJECTS).send_keys(subject)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.UPLOAD_PICTURE_FILE).send_keys(path)
        text = self.element_is_present(self.locators.UPLOAD_PICTURE_FILE).text
        f_name = file_name.split("/")[-1]
        # replace_path = text.split("\\")[-1]
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person_data.current_address)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(state)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        time.sleep(1)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(city)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(3)

        return [person_data.first_name + " " + person_data.last_name, person_data.email, person_data.phone_number, date_birth,
                subject, f_name, person_data.current_address, state, city]

    def check_registration_data_students(self) -> list:
        data_list = self.elements_are_visible(self.locators.RESULT_FILLS_FORM)
        check_list_reg_data = []

        for fill in data_list:
            check_list_reg_data.append(fill.text)

        return check_list_reg_data
