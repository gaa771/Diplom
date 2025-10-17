import pytest
import sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure

# Добавляем путь к main_test в sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))
from page.PageUI import PageUI
from config import driver


# Позитивный тест - поиск на кириллице
def test_find_cyrillic_positive_ui(driver):
    find = PageUI(driver)
    driver.implicitly_wait(30)
    result_cyrillic = find.find_cyrillic_positive_ui()
    assert result_cyrillic == "Аватар"

'''
# Позитивный тест - поиск на латинице
def test_find_latin_positive_ui(driver):
    find = PageUI(driver)
    driver.implicitly_wait(30)
    result_latin = find.find_latin_positive_ui()
    assert len(result_latin) > 0


# Позитивный тест - поиск по названию с цифрами
def test_find_figure_positive_ui(driver):
    find = PageUI(driver)
    driver.implicitly_wait(30)
    result_figure = find.find_figure_positive_ui()
    assert result_figure == "Форсаж\xa04"


# Негативный тест - поиск фильма с пустым названием
def test_find_empty_negative_ui(driver):
    find = PageUI(driver)
    driver.implicitly_wait(30)
    result_empty = find.find_empty_negative_ui()
    assert result_empty is True


# Негативный тест - поиск фильма со спецсимволами в названии
def test_find_special_character_negative_ui(driver):
    find = PageUI(driver)
    driver.implicitly_wait(30)
    result_special = find.find_special_character_negative_ui()
    assert result_special == "&"


# Негативный тест - поиск фильма с датой выпуска из будущего
def test_find_date_future_negative_ui(driver):
    find = PageUI(driver)
    driver.implicitly_wait(30)
    result_future = find.find_date_future_negative_ui()
    assert result_future is True


# Негативный тест - поиск фильма с использованием максимально
# возможного интервала годов выпуска
def test_find_max_date_negative_ui(driver):
    find = PageUI(driver)
    driver.implicitly_wait(30)
    result_max_date = find.find_max_date_negative_ui()
    assert len(result_max_date) > 0
'''
