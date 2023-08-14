import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

s = Service('C:\\Test\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
actions = ActionChains(driver)


@pytest.fixture(scope="module")
def web_driver_setup_teardown():
    driver.get('http://uitestingplayground.com/')
    driver.maximize_window()
