from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time
from tests.conftest import driver


def test_open_scenario_3(web_driver_setup_teardown):
    print("Открываем третий тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(1) > div:nth-of-type(3) > h3 > a").click()
    time.sleep(2)

def test_clic_to_button_by_xpath(web_driver_setup_teardown):
    print("Нажатие на зеленоую кнопку по XPATH")
    driver.find_element(By.XPATH, "//button[@id='greenButton']").click()

def test_repeat_button_click_by_xpath(web_driver_setup_teardown):
    print("Повторное нажатие на зеленую кнопку по XPATH")
    try:
        driver.find_element(By.XPATH, "//button[@id='greenButton']").click()
    except ElementClickInterceptedException:
        print("На зеленую кнопку больше не нажать")