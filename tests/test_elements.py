import time
from config import URL_PAGE_TEXT_BOX, URL_PAGE_CHECK_BOX
from pages.elements_page import TextBoxPage, CheckBox


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
            check_box = CheckBox(driver, URL_PAGE_CHECK_BOX)
            check_box.open()

            check_box.open_full_list()
            check_box.click_random_checkbox()
            check_box.get_checked_checkboxes()
            time.sleep(5)
