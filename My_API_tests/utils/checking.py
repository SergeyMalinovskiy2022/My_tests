"""Методы для проверки ответов запросв"""
import json

from requests import Response


class Checking():
    """Метод для проверки статус кода"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Статус код: " + str(response.status_code))
        else:
            print("Ошибка, статус код: " + str(response.status_code))

    """Метод для проверки наличия обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутсвуют")
