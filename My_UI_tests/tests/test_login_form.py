from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tests.conftest import driver


def test_open_scenario_13(web_driver_setup_teardown):
    print("Открываем тринадцатый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(4) > div:nth-of-type(2) > h3 > a").click()
    time.sleep(2)

def test_autorization(web_driver_setup_teardown):
    print("Ввод имени пользователя, пароля. и нажатие кнопки авторизации")
    driver.find_element(By.XPATH, "//section/div[@class='container']//input[@name='UserName']").send_keys("Ivan")
    driver.find_element(By.XPATH, "//section/div[@class='container']//input[@name='Password']").send_keys("pwd")
    driver.find_element(By.XPATH, "//button[@id='login']").click()

def test_check_autorization(web_driver_setup_teardown):
    print("Проверка успешной авторизации")
    cheking = driver.find_element(By.XPATH, "//label[@id='loginstatus']")
    print(cheking.text)