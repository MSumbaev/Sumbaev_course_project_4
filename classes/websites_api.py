from abc import ABC, abstractmethod
import requests
import time
import json

# Необходимо получить ТОКЕН SuperJob API и записать его в переменную окружения SUP_JOB_API_KEY
SUP_JOB_API_KEY = "v3.r.137650543.fe3caecc42c54edeee673c44f9f6a876873dbc25.3646af457c3f1f980e0297c8188c28921d80d383"


def printj(obj) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(obj, indent=2, ensure_ascii=False))


class WebsiteAPI(ABC):
    """ Абстрактный класс для работы с API сайтов с вакансиями"""

    @staticmethod
    @abstractmethod
    def get_vacancies(keyword, count_page):
        pass


class HeadHunterAPI(WebsiteAPI):
    """ Класс для работы с API hh.ru"""

    url = 'https://api.hh.ru/vacancies'

    @staticmethod
    def get_vacancies(keyword: str, count_page: int):
        """Возвращает 500 вакансий по России по ключевому слову keyword"""

        vacancies_hh = []

        params = {
            "text": keyword,
            "area": 113,
            "page": count_page,
            "per_page": 100
        }

        for page in range(count_page):

            response = requests.get(HeadHunterAPI.url, params=params)

            if response.status_code == 200:
                data = response.json()
                vacancies_hh.extend(data["items"])

                time.sleep(0.5)

            else:
                print(f"Request failed with status code: {response.status_code}")

        return vacancies_hh


class SuperJobAPI(WebsiteAPI):
    """ Класс для работы с API SuperJob"""

    url = 'https://api.superjob.ru/2.0/vacancies/'

    @staticmethod
    def get_vacancies(keyword: str, count_page: int):
        """Возвращает 500 вакансий по России по ключевому слову keyword"""

        vacancies_sj = []

        headers = {
            "X-Api-App-Id": SUP_JOB_API_KEY
        }

        params = {
            "keyword": keyword,
            "c": 1,
            "page": count_page,
            "count": 100,
        }

        for page in range(count_page):

            response = requests.get(SuperJobAPI.url, params=params, headers=headers)

            if response.status_code == 200:
                data = response.json()
                vacancies_sj.extend(data["objects"])

                time.sleep(0.5)

            else:
                print(f"Request failed with status code: {response.status_code}")

        return vacancies_sj
