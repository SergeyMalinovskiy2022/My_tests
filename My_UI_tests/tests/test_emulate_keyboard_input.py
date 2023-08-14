from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tests.conftest import driver


def test_open_scenario_8(web_driver_setup_teardown):
    print("Открываем восьмой тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > div:nth-of-type(4) > h3 > a").click()
    time.sleep(2)

def test_check_button_name(web_driver_setup_teardown):
    print("Проверка названия кнопки")
    element = driver.find_element(By.XPATH, "//button[@id='updatingButton']")
    element_text = element.text
    print("Текст Кнопки:", element_text)

def test_enter_text_by_xpath(web_driver_setup_teardown):
    print("Ввод данных в поле и изменение имени кнопки")
    driver.find_element(By.XPATH, "//input[@id='newButtonName']").send_keys("New name Button")
    driver.find_element(By.XPATH, "//button[@id='updatingButton']").click()


def test_check_button_new_name(web_driver_setup_teardown):
    print("Проверка что кнопка переименована")
    element = driver.find_element(By.XPATH, "//button[@id='updatingButton']")
    element_text = element.text
    print("Текст Кнопки:", element_text)