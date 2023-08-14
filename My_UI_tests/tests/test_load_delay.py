from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tests.conftest import driver


def test_open_scenario_4(web_driver_setup_teardown):
    print("Открываем четвертый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(1) > div:nth-of-type(4) > h3 > a").click()
    time.sleep(2)

def test_waiting_for_pages_to_load(web_driver_setup_teardown):
    print("Ожидание пока страница загрузится и нажатие на кнопку")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary']")))

