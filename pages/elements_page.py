import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators, \
    WebTableLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())

        full_name = person_info.full_name
        email = person_info.email
        current_adress = person_info.current_address
        permanent_adress = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_adress)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_adress)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_adress, permanent_adress

    def check_field_form(self):
        full_name = self.element_is_visible(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_visible(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_adress = self.element_is_visible(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_adress = self.element_is_visible(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_adress, permanent_adress


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = len(item_list)

        while count != 0:
            item = item_list[(random.randint(1, len(item_list) - 1))]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data_checked = []

        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data_checked.append(title_item.text)
        return str(data_checked).replace(' ', '').replace('.doc', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data_result = []

        for item in result_list:
            data_result.append(item.text)
        return str(data_result).lower().replace(' ', '')


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def clicked_on_the_radio_btn(self, choice):
        dict_radio_btn = {
            'yes': self.locators.YES_RADIO,
            'impressive': self.locators.IMPRESSIVE_RADIO,
            'no': self.locators.NO_RADIO
        }
        self.element_is_visible(dict_radio_btn[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTableLocators()

    def add_new_person(self):
        person_add = next(generated_person())

        first_name = person_add.first_name
        last_name = person_add.last_name
        email = person_add.email
        age = person_add.age
        salary = person_add.salary
        department = person_add.department

        self.element_is_visible(self.locators.ADD_BTN_PERSON).click()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SALARY).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
        self.element_is_visible(self.locators.SUBMIT_BTN).click()

        return [first_name, last_name, str(age), email, str(salary), department]

    def check_added_new_person(self):
        data = []
        persons = self.elements_are_visible(self.locators.PERSON_LIST)
        for person in persons:
            data.append(person.text.splitlines())
        return data

    def search_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_FIELD).clear()
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(key_word)

    def check_search_person(self):
        row = self.elements_are_visible(self.locators.PERSON_LIST)[0]
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        self.element_is_visible(self.locators.EDIT_RECORD_BUTTONT).click()
        self.element_is_visible(self.locators.FIRST_NAME).clear()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.SUBMIT_BTN).click()
        return first_name

    def click_delete_person_info(self):
        self.element_is_visible(self.locators.DELETE_RECORD_BUTTON).click()

    def check_delete_person_info(self):
        return self.element_is_visible(self.locators.DELETE_TEXT).text
