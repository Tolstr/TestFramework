import pytest, time
from selenium import webdriver

#Passed tests
def test_one_selenium():
    driver=webdriver.Chrome('C:\Tools\chromedriver.exe')
    driver.get('https://www.google.com')
    time.sleep(5)
    driver.quit()



def test_two():
    driver = webdriver.Chrome('C:\Tools\chromedriver.exe')
    driver.get('https://www.yahoo.com')
    time.sleep(5)
    driver.quit()
    pass

# failed tests
def test_three():
    assert False
def test_four():
    assert 0
# passed tests
def test_five():
    assert True
def test_six():
    assert 1

#Assertion test
def test_seven():
    assert 2 != 1

def test_eight():
    assert 2==2

def test_nine():
    assert 3==1

@pytest.mark.skip(reason='not working now')
def test_ten():
    assert 10==0

@pytest.mark.xfail(reason='test failing')
def test_eleven():
    assert 10==0

