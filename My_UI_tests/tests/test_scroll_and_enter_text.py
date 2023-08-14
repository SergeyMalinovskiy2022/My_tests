from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tests.conftest import driver



def test_open_scenario_16(web_driver_setup_teardown):
    print("Открываем шестнадцатый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(5) > div:nth-of-type(1) > h3 > a").click()
    time.sleep(2)


def test_enter_text_in_overlapped_element():
    print("Прокрутка вниз и ввод данных в поле")
    input_field = driver.find_element(By.XPATH, "//input[@id='name']")
    driver.execute_script("arguments[0].scrollIntoView();", input_field)

    entered_value = "ivan"
    input_field.send_keys(entered_value)

    actual_value = input_field.get_attribute("value")
    assert actual_value == entered_value
    print("Данные успешно введены в поле")
