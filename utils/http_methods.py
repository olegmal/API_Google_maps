import allure
import requests


""" List of HTTP methods"""

class HttpMethod:

    headers = {"Content-Type": 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):   # без self, тому що методи будуть статичними, тобто їх будуть визивати в будь-якому місці
        with allure.step("Method GET"):
            result = requests.get(url, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("Method POST"):
            result = requests.post(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("Method PUT"):
            result = requests.put(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("Method DELETE"):
            result = requests.delete(url, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookie)
            return result
