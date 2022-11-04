import time
import pytest
from config import URL

from pages.base_page import BasePage


def test_a(driver):
    page = BasePage(driver, URL)
    page.open()