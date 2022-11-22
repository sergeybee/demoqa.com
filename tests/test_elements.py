import time
from config import URL_PAGE_TEXT_BOX, URL_PAGE_CHECK_BOX, URL_PAGE_RADIO_BUTTON, URL_WEB_TABLE_PAGE
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, URL_PAGE_TEXT_BOX)
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_field_form()

            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current address does not match"
            assert permanent_address == output_per_addr, "the permanent address does not match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, URL_PAGE_CHECK_BOX)
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'Данные не совпадают'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_btn_page = RadioButtonPage(driver, URL_PAGE_RADIO_BUTTON)
            radio_btn_page.open()
            radio_btn_page.clicked_on_the_radio_btn('yes')
            out_yes = radio_btn_page.get_output_result()
            radio_btn_page.clicked_on_the_radio_btn('impressive')
            out_impressive = radio_btn_page.get_output_result()
            radio_btn_page.clicked_on_the_radio_btn('no')
            out_no = radio_btn_page.get_output_result()
            assert out_yes == 'Yes', "'Yes' have not been selected"
            assert out_impressive == 'Impressive', "'Impressive' have not been selected"
            assert out_no == 'No', "'No' have not been selected"
            time.sleep(3)

    class TestWebTables:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, URL_WEB_TABLE_PAGE)
            web_table_page.open()
            web_table_page.add_new_person()
