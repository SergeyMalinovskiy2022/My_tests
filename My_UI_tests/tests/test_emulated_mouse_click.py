from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tests.conftest import driver


def test_open_scenario_7(web_driver_setup_teardown):
    print("Открываем седьмой тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > div:nth-of-type(3) > h3 > a").click()
    time.sleep(2)

def test_clic_to_button_by_xpath(web_driver_setup_teardown):
    print("Нажатие на кнопку по XPATH")
    driver.find_element(By.XPATH, "/html//button[@id='badButton']").click()


def test_repeat_button_click_by_xpath(web_driver_setup_teardown):
    print("Повторное нажатие на кнопку которая поменяла цвет по XPATH")
    driver.find_element(By.XPATH, "/html//button[@id='badButton']").click()
