from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from tests.conftest import driver, s


def test_open_scenario_1(web_driver_setup_teardown):
    print("Открываем первый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(1) > div:nth-of-type(1) > h3 > a").click()
    time.sleep(2)

def test_clic_to_button_by_css(web_driver_setup_teardown):
    print("Нажатие на кнопку по CSS селектору")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

def test_clic_to_button_by_xpath(web_driver_setup_teardown):
    print("Нажатие на кнопку по XPATH")
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

def test_clic_to_button_by_id(web_driver_setup_teardown):
    print("Нажатие на кнопку по id")
    try:
        driver.find_element(By.ID, "8ccfa258-6758-667a-15bc-c623c7826b4f").click()
    except NoSuchElementException:
        print("Элемент не найден так как id динамичный")