from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from tests.conftest import driver

def test_open_scenario_9(web_driver_setup_teardown):
    print("Открываем девятый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(3) > div:nth-of-type(1) > h3 > a").click()
    time.sleep(2)

def test_click_button_in_scroll_view(web_driver_setup_teardown):
    print("Находим и нажимаем на кнопку в области прокрутки")
    actions = ActionChains(driver)
    button = driver.find_element(By.XPATH, "//button[@id='hidingButton']")
    actions.move_to_element(button).perform()
    button.click()
    time.sleep(2)



