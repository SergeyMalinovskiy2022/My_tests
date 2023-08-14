from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from tests.conftest import driver


def test_open_scenario_12(web_driver_setup_teardown):
    print("Открываем двенадцатый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > div:nth-of-type(4) > h3 > a").click()
    time.sleep(2)

def test_click_the_start_button():
    print("Нажатие на кнопку старт")
    driver.find_element(By.XPATH,"//button[@id='startButton']").click()

def test_click_the_stop_button_when_progress_is_75():
    print("Нажатие кнопки стоп когда прогресс будет 75 процентов")
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='progressBar' and  @aria-valuenow='75']")))
    driver.find_element(By.XPATH, "//button[@id='stopButton']").click()
    time.sleep(10)
