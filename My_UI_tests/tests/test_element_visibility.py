from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time
from tests.conftest import driver

def test_open_scenario_17(web_driver_setup_teardown):
    print("Открываем семнадцатый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(4) > div:nth-of-type(1) > h3 > a").click()
    time.sleep(2)


def test_make_sure_the_buttons_are_present_and_hide_button_functionality(web_driver_setup_teardown):
    hide_button = driver.find_element(By.XPATH, "//button[@id='hideButton']")
    removed_button = driver.find_element(By.XPATH, "//button[@id='removedButton']")
    zero_width_button = driver.find_element(By.XPATH, "//button[@id='zeroWidthButton']")
    overlapped_button = driver.find_element(By.XPATH, "//button[@id='overlappedButton']")
    transparent_button = driver.find_element(By.XPATH, "//button[@id='transparentButton']")
    invisible_button = driver.find_element(By.XPATH, "//button[@id='invisibleButton']")
    notdisplayed_button = driver.find_element(By.XPATH, "//button[@id='notdisplayedButton']")
    offscreen_button = driver.find_element(By.XPATH, "//button[@id='offscreenButton']")

    print("Проверка присутствия кнопок")
    assert hide_button.is_displayed()

    assert removed_button.is_displayed()
    assert zero_width_button.is_displayed()
    assert overlapped_button.is_displayed()
    assert transparent_button.is_displayed()
    assert invisible_button.is_displayed()
    assert notdisplayed_button.is_displayed()
    assert offscreen_button.is_displayed()
    print("Все кнопки присутствуют")

    print("Нажатие на кнопку Hide")
    hide_button.click()
    time.sleep(2)

    print("Проверка отсутствия остальных кнопок")
    try: removed_button.is_displayed() and zero_width_button.is_displayed() and overlapped_button.is_displayed() and \
         transparent_button.is_displayed() and invisible_button.is_displayed() and notdisplayed_button.is_displayed() \
         and offscreen_button.is_displayed()
    except StaleElementReferenceException:
        pass
        print("Все остальные кнопки скрыты")



