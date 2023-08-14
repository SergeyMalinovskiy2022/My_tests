from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
from tests.conftest import driver,actions


def test_open_scenario_18(web_driver_setup_teardown):
    print("Открываем восемнадцатый тестовый сценарий")
    driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(5) > div:nth-of-type(2) > h3 > a").click()
    time.sleep(2)


def test_generate_and_copy_guid(web_driver_setup_teardown):

    shadow_host = driver.find_element(By.XPATH, "//div/guid-generator")

    # Получить Shadow DOM элемент
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)

    # Найти элементы внутри Shadow DOM
    button_generate = shadow_root.find_element(By.CLASS_NAME, 'button-generate')
    button_copy = shadow_root.find_element(By.ID, 'buttonCopy')
    edit_field = shadow_root.find_element(By.CLASS_NAME, 'edit-field')

    # Нажать на кнопгу генерирующую GUID
    actions.move_to_element(button_generate).click().perform()
    time.sleep(2)

    # Нажать на кнопку копировать в буфер обмена
    actions.move_to_element(button_copy).click().perform()

    # Получить текст GUID из поля ввода
    guid_text = edit_field.get_attribute('value')

    # Кликнуть по полю ввода GUID, чтобы активировать его
    actions.move_to_element(edit_field).click().perform()

    # Выделить текст в поле ввода
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    # Копировать текст в буфер обмена
    actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

    # Получить текст из буфера обмена
    clipboard_text = pyperclip.paste()

    # Проверить, что текст из буфера обмена совпадает с GUID из поля ввода
    assert clipboard_text == guid_text, "GUID не скопирован в буфер обмена"