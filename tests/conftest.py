import pytest
from selenium import webdriver

@pytest.fixture(scope='session') #reduces code and repetition like do not need login every time or webdiver run once
def driver_init_fixture():
    driver = webdriver.Chrome(r'C:\Projects\boha_automation_portal\dependencies\chromedriver.exe')
    yield driver
    driver.quit()

@pytest.fixture(scope='session') #reduces code and repetition like do not need login every time or webdiver run once
def driver_init_fixture2():
    driver = webdriver.Chrome(r'C:\Projects\boha_automation_portal\dependencies\chromedriver.exe')
    yield driver
    driver.quit()