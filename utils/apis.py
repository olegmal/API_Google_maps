from utils.http_methods import HttpMethod

"""Methods to test google maps APIs"""

base_url = "https://rahulshettyacademy.com"
key = "?key =qaclick123"

class GoogleMap():

    @staticmethod
    def create_new_place():
        json_create_new_place = {
                "location": {
                "lat": -38.383494,
                "lng": 33.427362
                }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": [
                 "shoe park",
                "shop"
                 ],
                 "website": "http://google.com",
                "language": "French-IN"
                 }
        post_resource = "/maps/api/place/add/json" # ресурс методу post
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethod.post(post_url, json_create_new_place)
        print(result_post.text)
        return result_post

        """Метод для перевірки створення нової локації"""
    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethod.get(get_url)
        print(result_get.text)
        return result_get



        """Метод для оновлення нової локації"""
    @staticmethod
    def put_new_place(place_id):
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        json_to_update_location = {
                "place_id": place_id,
                 "address":"14 Khreschatic street, UKR",
                "key":"qaclick123"
                }

        result_put = HttpMethod.put(put_url, json_to_update_location)
        print(result_put.text)
        return result_put
        """Метод для видалення нової локації"""
    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_to_delete_location = {
            "place_id": place_id
        }

        result_delete = HttpMethod.delete(delete_url, json_to_delete_location)
        print(result_delete.text)
        return result_delete