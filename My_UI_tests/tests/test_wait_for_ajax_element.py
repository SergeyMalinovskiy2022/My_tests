from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from tests.conftest import driver


def test_open_scenario_5(web_driver_setup_teardown):
    print("Открываем пятый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > div:nth-of-type(1) > h3 > a").click()
    time.sleep(2)

def test_clic_to_button_by_xpath(web_driver_setup_teardown):
    print("Нажатие на зеленоую кнопку по XPATH")
    driver.find_element(By.XPATH, "//button[@id='ajaxButton']").click()


def test_waiting_for_element_to_appear(web_driver_setup_teardown):
    print("Ожидание появления данных")
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='content']/p")))
    element.click()
    element_text = element.text
    print("Текст элемента:", element_text)