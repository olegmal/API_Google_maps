from requests import Response
"""Методи для перевірки наших запитів"""

class Checking:

    """Метод для перевірки status code"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Вірно! Статуc код = "+ str(response.status_code))
        else:
            print("Халепа! Статуc код = "+ str(response.status_code))


