from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """ В классе BasePage определяются основные-частые действия для всего проекта.

    Methods
    _____
        open() - Открывает страницу в браузере
        element_is_visible() - Проверка того, что элемент присутствует в DOM страницы и виден.
        elements_are_visible() - Проверка того, что все элементы присутствуют в DOM страницы и видны.
        element_is_present() - Проверка того, что элемент присутствует в DOM страницы.
        elements_are_present() - Проверка наличия хотя бы одного элемента на веб-странице.
        elements_is_not_visible() - Проверка, что элемент либо невидим либо отсутствует в DOM.
        element_is_clickable() - Возвращает элемент когда он станет кликабельным, или вернет False в ином случае.
        go_to_element() - Делает скроллинг к нужному элементу страницы используя метод execute_script()

    """

    def __init__(self, driver, url):

        self.driver = driver
        self.url = url

    def open(self):
        """ Метод открывает страницу в браузере """

        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """
        Метод проверки того, что элемент присутствует в DOM страницы и виден.
        Видимость означает, что элемент не только отображается, но и имеет высоту и ширину, которые больше 0.
        Локатор - используется для поиска элемента, возвращает WebElement, когда он найден и виден.

        Используется метод element_to_be_clickable из модуля selenium.webdriver.support.expected_conditions

        locator -- Локатор искомого элемента на странице сайта
        timeout -- Время в течении которого метод будет ждать (default 5)

         """

        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """
        Метод проверки того, что все элементы присутствуют в DOM страницы и видны.
        Видимость означает, что элементы не только отображаются, но и имеют высоту и ширину, которые больше 0.
        Локатор - используется для поиска элементов, возвращает список WebElements, когда они найдены и видны.

        Используется метод element_to_be_clickable из модуля selenium.webdriver.support.expected_conditions

         """

        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        """
        Метод проверки того, что элемент присутствует в DOM страницы.
        Но это не обязательно означает, что элемент виден.
        Локатор - используется для поиска элемента, возвращает WebElement, когда он найден.

        Используется метод presence_of_element_located из модуля selenium.webdriver.support.expected_conditions

         """

        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """
        Метод проверки наличия хотя бы одного элемента на веб-странице.
        Но это не обязательно означает, что элемент виден.
        Локатор - используется для поиска элемента, возвращает список WebElements, когда они найдены.

        Используется метод presence_of_all_elements_located из модуля selenium.webdriver.support.expected_conditions

         """

        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def elements_is_not_visible(self, locator, timeout=5):
        """
        Метод проверяет, что элемент либо невидим либо отсутствует в DOM в течении заданного timeout'а.

        Используется метод invisibility_of_element_located из модуля selenium.webdriver.support.expected_conditions

         """

        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """
        Метод возвращает элемент когда он станет кликабельным, или вернет False в ином случае.

        Используется метод element_to_be_clickable из модуля selenium.webdriver.support.expected_conditions

         """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """ Делает скроллинг к нужному элементу страницы используя метод execute_script() """

        self.driver.execute_script("arguments[0].ScrollIntoView;", element)

    def action_double_click(self, element):
        """
        Метод делает двойной клик левой кнопкой мыши по элементу или текущей позиции.

        Используется класс ActionChains из selenium.webdriver и его метод double_click(on_element=None)

        on_element=element – The element to click.
        on_element=None - If None, clicks on current mouse position.

        """
        # Создаем объект цепочки действий
        action = ActionChains(self.driver)

        # Дважды кликнуть по элементу
        action.double_click(element)

        # Производит выполнение операции
        action.perform()

    def action_right_click(self, element):
        """
        Метод делает клик правой кнопкой мыши по элементу или текущей позиции.

        Используется класс ActionChains из selenium.webdriver и его метод context_click(on_element=element)

        on_element=element – The element to click.
        on_element=None - If None, clicks on current mouse position.

         """

        # Создаем объект цепочки действий
        action = ActionChains(self.driver)

        # Дважды кликнуть по элементу
        action.context_click(element)

        # Производит выполнение операции
        action.perform()
