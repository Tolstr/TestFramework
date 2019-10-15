import pytest, time
from selenium import webdriver

class TestHyi:
    def test_f_one(self,driver_init_fixture):
        self.driver = driver_init_fixture
        self.driver.get('https://www.google.com')
        time.sleep(2)

    def test_f_two(self, driver_init_fixture2):
        self.driver = driver_init_fixture2
        self.driver.get('https://www.gmail.com')
        time.sleep(2)


