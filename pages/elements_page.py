import base64
import os
import random
import time
import requests

from selenium.common import TimeoutException

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import *
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
    locators = RadioButtonPageLocators()

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
    locators = WebTablePageLocators()

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

    def check_count_rows(self):
        return self.element_is_visible(self.locators.PERSON_LIST)

    def change_count_row(self):
        row_count = [5, 10, 20, 25, 50, 100]
        rows_data = []
        for rows in row_count:
            row_value = self.element_is_present(self.locators.CHANGE_VALUE)
            self.go_to_element(self.locators.CHANGE_VALUE)
            row_value.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{rows}"]')).click()
            rows_data.append(self.check_count_rows())
        return rows_data


class ButtonPage(BasePage):
    locators = ButtonPageLocators()

    def check_clicked_btn(self, element):
        return self.element_is_visible(element).text

    def double_click_on_btn(self):
        btn = self.element_is_visible(self.locators.DOUBLE_CLICK_BTN)
        self.action_double_click(btn)
        return self.check_clicked_btn(self.locators.DOUBLE_CLICK_BTN_TEXT)

    def right_click_on_btn(self):
        btn = self.element_is_visible(self.locators.RIGHT_CLICK_BTN)
        self.action_right_click(btn)
        return self.check_clicked_btn(self.locators.RIGHT_CLICK_BTN_TEXT)

    def click_on_btn_click_me(self):
        self.element_is_visible(self.locators.CLICK_ME_BTN).click()
        return self.check_clicked_btn(self.locators.CLICK_ME_BTN_TEXT)


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def should_be_open_simple_link_in_new_tab(self):
        """ Проверяем, что открывается страница сайта "https://demoqa.com/" """
        link_home = self.element_is_visible(self.locators.SIMPLE_LINK)
        href = link_home.get_attribute('href')
        link_home.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        url = self.driver.current_url
        assert href == url, "Исходный адрес не совпадает с адресом открытый в новой вкладке"

    def should_be_open_dinamyc_link_in_new_tab(self):
        """ Проверяем, что открывается страница сайта "https://demoqa.com/" """
        link_home = self.element_is_visible(self.locators.DYNAMIC_LINK)
        href = link_home.get_attribute('href')
        link_home.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        url = self.driver.current_url
        assert href == url, "Исходный адрес не совпадает с адресом открытый в новой вкладке"

    def check_status_created_link(self):
        create_link = self.element_is_visible(self.locators.CREATED_LINK)
        create_link.click()
        r = requests.get('https://demoqa.com/created')
        assert r.status_code == 201, "    "

    def check_status_no_content_link(self):
        create_link = self.element_is_visible(self.locators.NO_CONTENT_LINK)
        create_link.click()
        r = requests.get('https://demoqa.com/no-content')
        assert r.status_code == 204, "    "

    def check_status_moved_link(self):
        create_link = self.element_is_visible(self.locators.MOVED_LINK)
        create_link.click()
        r = requests.get('https://demoqa.com/moved')
        assert r.status_code == 301, "    "

    def check_status_bad_request_link(self):
        create_link = self.element_is_visible(self.locators.BAD_REQUEST_LINK)
        create_link.click()
        r = requests.get('https://demoqa.com/bad-request')
        assert r.status_code == 400, "    "

    def check_status_unauthorized_link(self):
        create_link = self.element_is_visible(self.locators.UNAUTHORIZED_LINK)
        create_link.click()
        r = requests.get('https://demoqa.com/unauthorized')
        assert r.status_code == 401, "    "

    def check_status_forbidden_link(self):
        create_link = self.element_is_visible(self.locators.FORBIDDEN_LINK)
        create_link.click()
        r = requests.get('https://demoqa.com/forbidden')
        assert r.status_code == 403, "    "

    def check_status_invalid_url_link(self):
        create_link = self.element_is_visible(self.locators.INVALID_URL_LINK)
        create_link.click()
        r = requests.get('https://demoqa.com/invalid-url')
        assert r.status_code == 404, "    "


class DownloadUploadPage(BasePage):
    locators = DownloadUploadPageLocators()

    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE_BTN).get_attribute('href').split(',')
        link_decode = base64.b64decode(link[1])

        path_file = f"/home/user/py/myapp/demoqa.com/file{random.randint(0, 999)}.jpeg"

        with open(path_file, 'wb+') as f:
            f.write(link_decode)
            check_file = os.path.exists(path_file)
            f.close()
            os.remove(path_file)
        return check_file

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE_BTN).send_keys(path)
        text = self.element_is_present(self.locators.UPLOADED_FILE_NAME_TEXT).text
        f_name = file_name.split("/")[-1]
        replace_path = text.split("\\")[-1]
        os.remove(path)
        return f_name, replace_path


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    def check_clickable_enable_btn(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_BTN)
        except TimeoutException:
            return False
        return True

    def change_color_text_btn(self):
        text_color_btn = self.element_is_present(self.locators.COLOR_TEXT_BTN)
        before_color = text_color_btn.value_of_css_property('color')
        time.sleep(8)
        after_color = text_color_btn.value_of_css_property('color')
        assert before_color != after_color, "Цвет текста кнопки должен не совпадать"

    def check_appear_of_button(self):
        try:
            self.element_is_clickable(self.locators.VISIBLE_AFTER_FIVE_SEC_BTN)
        except TimeoutException:
            return False
        return True
