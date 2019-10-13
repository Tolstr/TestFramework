import pytest, time
from selenium import webdriver



@pytest.fixture(scope='session') #reduces code and repetition like do not need login every time or webdiver run once
def driver_init_fixture():
    driver = webdriver.Chrome('C:\Tools\chromedriver.exe')
    return driver


def test_fixture_one(driver_init_fixture):
    driver = driver_init_fixture
    driver.get('https://www.google.com')
    time.sleep(2)


def test_fixture_two(driver_init_fixture):
    driver = driver_init_fixture
    driver.get('https://www.yahoo.com')
    time.sleep(2)


