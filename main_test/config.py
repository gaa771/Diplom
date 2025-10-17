import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from settings import API_KEY


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


# Авторизация
@pytest.fixture
def headers():
    return {
        "X-API-KEY": API_KEY,
        "accept": 'application/json'
    }
