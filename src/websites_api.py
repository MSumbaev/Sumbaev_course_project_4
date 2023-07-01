from abc import ABC, abstractmethod
import requests
import time
import json


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class WebsiteAPI(ABC):
    """ Абстрактный класс для работы с API сайтов с вакансиями"""

    @staticmethod
    @abstractmethod
    def get_vacancies(keyword: str):
        pass


class HeadHunterAPI(WebsiteAPI):
    """ Класс для работы с API hh.ru"""

    url = 'https://api.hh.ru/vacancies'

    @staticmethod
    def get_vacancies(keyword: str):
        """Возвращает 1000 вакансий по России по ключевому слову keyword"""

        vacancies = []

        for page in range(10):

            params = {
                "text": keyword,
                "area": 113,
                "page": page,
                "per_page": 10  # Поменять на 100!!!
            }

            response = requests.get(HeadHunterAPI.url, params=params)

            if response.status_code == 200:
                data = response.json()
                vacancies.extend(data["items"])

                time.sleep(0.1)

            else:
                print(f"Request failed with status code: {response.status_code}")

        return vacancies


class SuperJobAPI(WebsiteAPI):
    """ Класс для работы с API hh.ru"""

    def get_vacancies(self, key_word: str):
        pass
