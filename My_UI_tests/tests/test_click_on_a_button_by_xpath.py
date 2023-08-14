from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from tests.conftest import driver


def test_open_scenario_2(web_driver_setup_teardown):
    print("Открываем второй тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(1) > div:nth-of-type(2) > h3 > a").click()
    time.sleep(2)

def test_click_to_button_by_xpath(web_driver_setup_teardown):
    print("Нажатие на кнопку по XPATH")
    driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')][1]").click()
    time.sleep(5)

def test_accept_alert(web_driver_setup_teardown):
    print("Подтверждение в браузере")
    alert = driver.switch_to.alert
    alert.accept()