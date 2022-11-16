import time
from config import URL_TEXT_BOX
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox():
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, URL_TEXT_BOX)
            text_box_page.open()
            text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_adress = text_box_page.check_field_form()
            time.sleep(5)
