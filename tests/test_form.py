import time

from pages.form_page import RegistrationStudentForm
from config import URL_FORM_PAGE


class TestFormPage:

    class TestFormRegistrationStudent:
        def test_filling_data_in_the_form_fields(self, driver):
            reg_form_page = RegistrationStudentForm(driver, URL_FORM_PAGE)
            reg_form_page.open()
            person = reg_form_page.fills_data_in_the_form_fields()
            time.sleep(2)
            result = reg_form_page.check_registration_data_students()
            print(person)
            print(result)