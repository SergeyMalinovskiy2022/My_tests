from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from tests.conftest import driver



def test_open_scenario_14(web_driver_setup_teardown):
    print("Открываем четырнадцатый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(4) > div:nth-of-type(3) > h3 > a").click()
    time.sleep(2)

def test_dubble_click_to_element():
    print("Навести курсор на элемент и 2 раза нажать на него затем проверить что было 2 нажатия")
    actions = ActionChains(driver)
    element_click_me = driver.find_element(By.XPATH, "//section//a[@title='Click me']")
    actions.move_to_element(element_click_me).double_click().perform()
    check_the_number_of_clicks = driver.find_element(By.XPATH, "//span[@id='clickCount']")
    clicks_count = check_the_number_of_clicks.text
    print(f"Количество кликов: {clicks_count}")
    check_the_number_of_clicks == "2"
