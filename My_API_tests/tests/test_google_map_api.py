from utils.api import GoogleMapsApi
from requests import Response

"""Создание изменение и удаление новой локации"""


class TestCratePlace():

    def test_create_new_place(self):
        print("Метод POST")
        result_post: Response = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("Метод GET POST")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        print("Метод PUT")
        result_put: Response = GoogleMapsApi.put_new_place(place_id)

        print("Метод GET PUT")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        print("Метод Delete")
        result_delete: Response = GoogleMapsApi.delete_new_place(place_id)

        print("Метод GET Delete")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)


