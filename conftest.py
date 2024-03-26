import pytest
from selenium import webdriver
from data import Paths

def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox", type=str)

# Фикстура получения и закрытия driver
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = None
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    driver.get(Paths.YANDEX_SCOOTER_URL)
    yield driver
    driver.quit()