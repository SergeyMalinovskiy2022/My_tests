from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tests.conftest import driver


def test_open_scenario_10(web_driver_setup_teardown):
    print("Открываем десятый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > div:nth-of-type(2) > h3 > a").click()
    time.sleep(2)


def test_get_cpu_load_for_chrome(web_driver_setup_teardown):
    print("Находим CPU для Chrome и сравниваем с значением выделеным желтым цветом")

    # Находим строку Chrome
    chrome_row = driver.find_element(By.XPATH,
                                     "//div[@role='rowgroup']//span[@role='cell' and contains(text(), 'Chrome')]/ancestor::div[@role='row']")

    # Получаем все ячейки строки Chrome
    chrome_cells = chrome_row.find_elements(By.XPATH, ".//span[@role='cell']")

    # Находим значение CPU в строке Chrome, которое заканчивается на "%"
    cpu_value = None
    for cell in chrome_cells:
        if cell.text.endswith("%"):
            cpu_value = cell.text
            break

    # Находим желтое значение CPU для Chrome
    yellow_cpu_value = driver.find_element(By.XPATH, "//p[@class='bg-warning']").text
    yellow_cpu_value = yellow_cpu_value.split(":")[1].strip()

    # Сравниваем значения
    assert cpu_value == yellow_cpu_value, \
        f"Значение CPU для Chrome не совпадает: ожидалось {yellow_cpu_value}, получено {cpu_value}"



