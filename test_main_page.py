from main_page import MainPage
import pytest
import time
from locators import MainPageLocators


def test_page_open(browser):
    link = "https://csgoempire.com"
    # link = "https://www.google.ru/"
    page = MainPage(browser, link)
    # Открываем страницу, на которой будем парсить
    page.open()
    # Открываем страницу, на которой будем парсить
    time.sleep(10)

    while True:
        page.wait_for_counter_disappear(*MainPageLocators.COUNTER)
        page.watch_the_wheel(browser, *MainPageLocators.WHEEL)
        page.collect_data(browser, *MainPageLocators.RESULT)
        # page.wait_for_counter(*MainPageLocators.COUNTER)



