from pages.form_page import RegistrationStudentForm
from config import URL_REGISTRATION_FORM_PAGE
from locators.form_page_locators import RegistrationFormPageLocators


class TestRegistrationStudentFormPage:
    def test_for_filling_data_in_the_form_fields(self, driver):
        reg_form_page = RegistrationStudentForm(driver, URL_REGISTRATION_FORM_PAGE)
        reg_form_page.open()
        fill_data = reg_form_page.fills_in_the_data_in_the_form_fields()
        check_data = reg_form_page.check_registration_data_students()

        assert fill_data == check_data, ""
