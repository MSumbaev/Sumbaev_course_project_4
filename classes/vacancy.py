class Vacancy:
    def __init__(self, vacancy):
        self.name = vacancy["name"]
        self.salary_from = vacancy["salary_from"]
        self.salary_to = vacancy["salary_to"]
        self.currency = vacancy["currency"]
        self.city = vacancy["city"]
        self.url = vacancy["url"]
        self.employer = vacancy["employer"]
        self.requirement = vacancy["requirement"]
        self.api = vacancy["API"]

    def __str__(self):
        return f"""
{"**********" * 5}
Название вакансии: {self.name}
Зарплата от: {self.salary_from} {self.currency if self.currency == "RUB" else ""}
Зарплата до: {self.salary_to} {self.currency if self.currency == "RUB" else ""}
Город: {self.city}
url: {self.url}
Работодатель: {self.employer}
Требования: {self.requirement}
Вакансия найдена на: {self.api}
{"**********" * 5}
"""

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __ge__(self, other):
        return self.salary_from >= other.salary_from
