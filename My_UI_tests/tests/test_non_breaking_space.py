from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tests.conftest import driver



def test_open_scenario_15(web_driver_setup_teardown):
    print("Открываем пятнадцатый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(4) > div:nth-of-type(4) > h3 > a").click()
    time.sleep(2)


def test_find_button_with_non_breaking_space():
    print("Поиск кнопки с использованием неразрывного пробела в тексте")

    non_breaking_space = u'\u00A0'
    button_xpath = f"//button[text()='My{non_breaking_space}Button']"

    button_element = driver.find_element(By.XPATH, button_xpath)
    print("Кнопка найдена:", button_element.text)