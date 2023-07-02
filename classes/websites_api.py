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
        """Возвращает вакансии по России по ключевому слову keyword"""

        vacancies_hh = []

        params = {
            "text": keyword,
            "area": 113,
            "page": count_page,
            "per_page": 100,
            "archive": False
        }

        for page in range(count_page):

            response = requests.get(HeadHunterAPI.url, params=params)

            if response.status_code == 200:
                data = response.json()
                vacancies_hh.extend(data["items"])

                time.sleep(0.2)

            else:
                print(f"Request failed with status code: {response.status_code}")

        return vacancies_hh

    @staticmethod
    def formatted_vacancies(vacancies_hh):

        res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        dollar_rate = res['Valute']['USD']['Value']
        euro_rate = res['Valute']['EUR']['Value']

        formatted_vacancies = []

        for v in vacancies_hh:
            formatted_v = dict()
            formatted_v["name"] = v["name"]

            if v["salary"] is None:
                formatted_v["salary_from"] = "Не указано"
                formatted_v["salary_to"] = "Не указано"
                formatted_v["currency"] = "RUB"
            elif v["salary"]["currency"] == "RUR":
                formatted_v["salary_from"] = "Не указано" if v["salary"]["from"] is None else v["salary"]["from"]
                formatted_v["salary_to"] = "Не указано" if v["salary"]["to"] is None else v["salary"]["to"]
                formatted_v["currency"] = "RUB"
            elif v["salary"]["currency"] == "USD":
                formatted_v["salary_from"] = "Не указано" if v["salary"]["from"] is None else v["salary"][
                                                                                                  "from"] * dollar_rate
                formatted_v["salary_to"] = "Не указано" if v["salary"]["to"] is None else v["salary"][
                                                                                              "to"] * dollar_rate
                formatted_v["currency"] = "RUB"
            elif v["salary"]["currency"] == "EUR":
                formatted_v["salary_from"] = "Не указано" if v["salary"]["from"] is None else v["salary"][
                                                                                                  "from"] * euro_rate
                formatted_v["salary_to"] = "Не указано" if v["salary"]["to"] is None else v["salary"][
                                                                                              "to"] * euro_rate
                formatted_v["currency"] = "RUB"
            elif v["salary"]["currency"] not in ["EUR", "USD", "RUR"]:
                formatted_v["salary_from"] = "Не указано"
                formatted_v["salary_to"] = "Не указано"
                formatted_v["currency"] = "Не известная валюта для уточнения перейдите по ссылке"

            formatted_v["city"] = "Не указанно" if v["address"] is None else v["address"]["city"]
            formatted_v["url"] = v["alternate_url"]
            formatted_v["employer"] = v["employer"]["name"]
            formatted_v["requirement"] = v["snippet"]["requirement"]
            formatted_v["API"] = "HeadHunter"

            formatted_vacancies.append(formatted_v)

        return formatted_vacancies


class SuperJobAPI(WebsiteAPI):
    """ Класс для работы с API SuperJob"""

    url = 'https://api.superjob.ru/2.0/vacancies/'

    @staticmethod
    def get_vacancies(keyword: str, count_page: int):
        """Возвращает вакансии по России по ключевому слову keyword"""

        vacancies_sj = []

        headers = {
            "X-Api-App-Id": SUP_JOB_API_KEY
        }

        params = {
            "keyword": keyword,
            "c": [1],
            "page": count_page,
            # "count": 100,
            "archive": False
        }

        for page in range(count_page * 5):

            response = requests.get(SuperJobAPI.url, params=params, headers=headers)

            if response.status_code == 200:
                data = response.json()
                vacancies_sj.extend(data["objects"])

                time.sleep(0.1)

            else:
                print(f"Request failed with status code: {response.status_code}")

        return vacancies_sj

    @staticmethod
    def formatted_vacancies(vacancies_sj):

        formatted_vacancies = []

        for v in vacancies_sj:
            formatted_v = dict()
            formatted_v["name"] = v["profession"]
            formatted_v["salary_from"] = v["payment_from"]
            formatted_v["salary_to"] = v["payment_to"]
            formatted_v["currency"] = "RUB" if v["currency"] == "rub" else None
            formatted_v["city"] = v["client"]["town"]["title"]
            formatted_v["url"] = v["link"]
            formatted_v["employer"] = v["client"]["title"]
            formatted_v["requirement"] = v["candidat"]
            formatted_v["API"] = "SuperJob"

            formatted_vacancies.append(formatted_v)

        return formatted_vacancies
