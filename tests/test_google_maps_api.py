from requests import Response
import allure
import json
from utils.apis import GoogleMap
from utils.checking import Checking

@allure.epic("Test of creation new place location ")
class Test_create_place():

    @allure.description("Test of creation, update and delete of new place location")
    def test_create_new_place(self):

        print("Метод post")
        result_post: Response = GoogleMap.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)


        print("Метод GET-перевірка методу POST")
        result_get: Response = GoogleMap.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)


        print("Метод put")
        result_put: Response = GoogleMap.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)


        print("Метод GET- перевірка методу PUT")
        result_get: Response = GoogleMap.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)


        print("Метод DELETE")
        result_delete: Response = GoogleMap.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)

        print("Метод GET- перевірка методу DELETE")
        result_get: Response = GoogleMap.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)