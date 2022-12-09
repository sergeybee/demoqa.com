from locators.form_page_locators import RegistrationFormPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person


class RegistrationStudentForm(BasePage):
    """Форма регистрации студентов"""

    locators = RegistrationFormPageLocators()

    def fills_in_the_data_in_the_form_fields(self):
        person_data = next(generated_person())

        first_name = person_data.first_name
        last_name = person_data.last_name
        email = person_data.email
        phone_number = person_data.phone_number
        date_of_birth = person_data.date_of_birth
        current_address = person_data.current_address

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.USER_EMAIL).send_keys(email)
        self.element_is_visible(self.locators.USER_PHONE_NUMBER).send_keys(phone_number)
        self.element_is_visible(self.locators.DATE_OF_BIRTH).send_keys(date_of_birth)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)

        self.element_is_visible(self.locators.SUBMIT)

        return [first_name, last_name, email, phone_number, date_of_birth, current_address]

    def check_registration_data_students(self) -> list:

        data_list = self.element_is_visible(self.locators.CREATED_LIST_DATA)
        check_list_reg_data = []

        for tr in data_list:
            d = tr[1].text
            check_list_reg_data.append(d)

        return check_list_reg_data
