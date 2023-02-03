import random
import time

from config import *
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage, LinksPage, \
    DownloadUploadPage, DynamicPropertiesPage


class TestElements:
    """ Тестовый класс TestElements """

    class TestTextBox:
        """
        Тесты для текстовых (TextBox) полей формы на странице TextBox

        URL_PAGE_TEXT_BOX - Урл страницы
        """

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
        """
        Тесты для чек-боксов (CheckBox) на странице CheckBox

        URL_PAGE_CHECK_BOX - Урл страницы
        """

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, URL_PAGE_CHECK_BOX)
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'Данные не совпадают'

    class TestRadioButton:
        """
        Тесты для радио-батонов (RadioButton) на странице RadioButton

        URL_PAGE_RADIO_BUTTON - Урл страницы
        """

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
        """
        Тесты на добавление, редактирование, поиск, удаление человека в таблице на странице WebTables

        URL_WEB_TABLE_PAGE - Урл страницы
        """

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, URL_WEB_TABLE_PAGE)
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_added_new_person()
            assert new_person in table_result, 'Персона не найдена в таблице. Не добавлена'

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, URL_WEB_TABLE_PAGE)
            web_table_page.open()
            keyword_search = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_person(keyword_search)
            search_result = web_table_page.check_search_person()
            assert keyword_search in search_result, 'Искомая персона не найдена в таблице'

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, URL_WEB_TABLE_PAGE)
            web_table_page.open()
            web_table_page.add_new_person()
            update_data = web_table_page.update_person_info()
            web_table_page.search_person(update_data)
            search_result = web_table_page.check_search_person()
            assert update_data in search_result, "Обновленная информация о персоне, не найдена"

        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePage(driver, URL_WEB_TABLE_PAGE)
            web_table_page.open()
            person = web_table_page.add_new_person()[0]
            web_table_page.search_person(person)
            web_table_page.click_delete_person_info()
            result_check = web_table_page.check_delete_person_info()
            assert result_check == "No rows found", 'Персона не удалена'

        def test_web_table_change_rows(self, driver):
            web_table_page = WebTablePage(driver, URL_WEB_TABLE_PAGE)
            web_table_page.open()
            result_change_rows = web_table_page.change_count_row()
            assert result_change_rows == [5, 10, 20, 25, 50,
                                          100], "Кол-во строк в таблице не совпадают с выбранными или некорректны"

    class TestButtonsPage:
        """
        Тесты для кнопок на странице ButtonsPage

        URL_BUTTONS_PAGE - Урл страницы
        """

        def test_double_click_on_btn(self, driver):
            buttons_page = ButtonPage(driver, URL_BUTTONS_PAGE)
            buttons_page.open()
            result = buttons_page.double_click_on_btn()
            assert result == "You have done a double click"

        def test_right_click_on_btn(self, driver):
            buttons_page = ButtonPage(driver, URL_BUTTONS_PAGE)
            buttons_page.open()
            result = buttons_page.right_click_on_btn()
            assert result == "You have done a right click"

        def test_click_on_btn_click_me(self, driver):
            buttons_page = ButtonPage(driver, URL_BUTTONS_PAGE)
            buttons_page.open()
            result = buttons_page.click_on_btn_click_me()
            assert result == "You have done a dynamic click", "Ожидаемое сообщение не верное"

    class TestLinksPage:
        """
        Тесты для ссылок на странице LinksPage

        URL_LINKS_PAGE - Урл страницы
        """

        def test_simple_link_open_new_tab(self, driver):
            link_page = LinksPage(driver, URL_LINKS_PAGE)
            link_page.open()
            link_page.should_be_open_simple_link_in_new_tab()

        def test_dinamyc_link_open_to_new_tab(self, driver):
            link_page = LinksPage(driver, URL_LINKS_PAGE)
            link_page.open()
            link_page.should_be_open_dinamyc_link_in_new_tab()

        def test_status_created_link(self, driver):
            link_page = LinksPage(driver, URL_LINKS_PAGE)
            link_page.open()
            link_page.check_status_created_link()

        def test_status_no_content_link(self, driver):
            link_page = LinksPage(driver, URL_LINKS_PAGE)
            link_page.open()
            link_page.check_status_no_content_link()

        def test_status_moved_link(self, driver):
            link_page = LinksPage(driver, URL_LINKS_PAGE)
            link_page.open()
            link_page.check_status_moved_link()

        def test_status_bad_request_link(self, driver):
            link_page = LinksPage(driver, URL_LINKS_PAGE)
            link_page.open()
            link_page.check_status_bad_request_link()

        def test_status_unauthorized_link(self, driver):
            link_page = LinksPage(driver, URL_LINKS_PAGE)
            link_page.open()
            link_page.check_status_unauthorized_link()

    class TestDownloadUploadPage:
        """
        Тесты для скачивания и загрузки файлов на странице DownloadUploadPage

        URL_DOWNLOAD_UPLOAD_PAGE - Урл страницы
        """

        def test_download_file(self, driver):
            down_up_load_page = DownloadUploadPage(driver, URL_DOWNLOAD_UPLOAD_PAGE)
            down_up_load_page.open()
            check = down_up_load_page.download_file()
            assert check is True,  "Файл не был скачан / The file has not been downloaded"

        def test_upload_file(self, driver):
            down_up_load_page = DownloadUploadPage(driver, URL_DOWNLOAD_UPLOAD_PAGE)
            down_up_load_page.open()
            file_name, text_path = down_up_load_page.upload_file()
            assert file_name == text_path, "Файл не был загружен / The file has not been uploaded"

    class TestDynamicPropertiesPage:
        """
        Тесты для динамически изменяемых свойств текста, кнопок на странице DynamicPropertiesPage

        URL_DYNAMIC_PROPERTIES_PAGE - Урл страницы
        """

        def test_clickable_enable_btn(self, driver):
            dynamic_prop_page = DynamicPropertiesPage(driver, URL_DYNAMIC_PROPERTIES_PAGE)
            dynamic_prop_page.open()
            enable = dynamic_prop_page.check_clickable_enable_btn()
            assert enable is True

        def test_change_color_text_btn(self, driver):
            dynamic_prop_page = DynamicPropertiesPage(driver, URL_DYNAMIC_PROPERTIES_PAGE)
            dynamic_prop_page.open()
            dynamic_prop_page.change_color_text_btn()

        def test_appear_of_btn(self, driver):
            dynamic_prop_page = DynamicPropertiesPage(driver, URL_DYNAMIC_PROPERTIES_PAGE)
            dynamic_prop_page.open()
            appear = dynamic_prop_page.check_appear_of_button()
            assert appear is True



