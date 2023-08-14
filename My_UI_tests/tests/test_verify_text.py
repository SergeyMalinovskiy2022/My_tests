from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tests.conftest import driver



def test_open_scenario_11(web_driver_setup_teardown):
    print("Открываем одинадцатый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > div:nth-of-type(3) > h3 > a").click()
    time.sleep(2)

def test_find_element_by_text():
    print("Найти элемент по тексту внутри")
    element = driver.find_element(By.XPATH, "//div/span[normalize-space(.)='Welcome UserName!']")
    print(f"Текст элемента : {element.text}")