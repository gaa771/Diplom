import requests
import pytest
from settings import BASE_URL_1, BASE_URL_2, BASE_URL_3, API_KEY


# Авторизация
@pytest.fixture
def headers():
    return {
        "X-API-KEY": API_KEY,
        "accept": 'application/json'
    }


# Позитивный тест - поиск на кириллице
def test_find_cyrillic_positive(headers):
    base_url_loc = BASE_URL_1 + "Аватар"
    response = requests.get(base_url_loc, headers=headers)

    assert response.status_code == 200


# Позитивный тест - поиск на латинице
def test_find_latin_positive(headers):
    base_url_loc = BASE_URL_1 + "Warcraft"
    response = requests.get(base_url_loc, headers=headers)

    assert response.status_code == 200


# Позитивный тест - поиск по названию с цифрами
def test_find_figure_positive(headers):
    base_url_loc = BASE_URL_1 + "Форсаж 4"
    response = requests.get(base_url_loc, headers=headers)

    assert response.status_code == 200


# Негативный тест - поиск фильма с пустым названием
def test_find_empty_negative(headers):
    base_url_loc = BASE_URL_2 + "name=null"
    response = requests.get(base_url_loc, headers=headers)

    assert response.status_code == 200


# Негативный тест - поиск фильма со спецсимволами в названии
def test_find_special_character_negative(headers):
    base_url_loc = BASE_URL_2 + "name=#"
    response = requests.get(base_url_loc, headers=headers)

    assert response.status_code == 200


# Негативный тест - поиск фильма с датой выпуска из будущего
def test_find_date_future_negative(headers):
    base_url_loc = BASE_URL_3 + "year=2100"
    response = requests.get(base_url_loc, headers=headers)

    assert response.status_code == 400


# Негативный тест - поиск фильма с использованием максимально
# возможного интервала годов выпуска
def test_find_max_date_negative(headers):
    base_url_loc = BASE_URL_3 + "sortField=year&sortType=1&year=1900-2028"
    response = requests.get(base_url_loc, headers=headers)

    assert response.status_code == 200
