import json
from abc import ABC, abstractmethod
from classes.vacancy import Vacancy


class FileSaver(ABC):
    """Абстрактный класс для работы с вакансиями в файлах"""

    @abstractmethod
    def create_file(self, found_vacancies: list) -> None:
        """Сохранение списка вакансий в файл"""
        pass

    @abstractmethod
    def add_vacancies(self, data_vacancies: list) -> None:
        """Добавление вакансий в файл"""
        pass

    @abstractmethod
    def clean_file(self) -> None:
        """Очищает файл с вакансиями"""
        pass


class JSONSaver(FileSaver):
    """Класс для работы с вакансиями в json файле"""

    def __init__(self, file_name: str):
        self.file_name = file_name

    def create_file(self, found_vacancies: list) -> None:
        """Сохранение списка вакансий в json файл"""
        with open(f'data/{self.file_name}.json', 'w', encoding='utf-8') as f:
            json.dump(found_vacancies, f, indent=2, ensure_ascii=False)
        print("Файл сохранен в папку data/.")

    def add_vacancies(self, data_vacancies: list) -> None:
        """Добавление вакансий в json файл. Если файл не существует, создает его."""
        try:
            with open(f'data/{self.file_name}.json', 'r', encoding='utf-8') as f:
                data = json.loads(f.read())

            data.extend(data_vacancies)

            with open(f'data/{self.file_name}.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print("Операция прошла успешно")
        except FileNotFoundError:

            with open(f'data/{self.file_name}.json', 'w', encoding='utf-8') as f:
                json.dump(data_vacancies, f, indent=2, ensure_ascii=False)

    def clean_file(self) -> None:
        """Очищает файл с вакансиями"""
        with open(f'data/{self.file_name}.json', 'w', encoding='utf-8') as f:
            f.write("")

    def choose_all(self):
        """Возвращает список всех вакансий из файла в виде экземпляра класса Vacancy()"""
        with open(f'data/{self.file_name}.json', 'r', encoding='utf-8') as f:
            all_vacancies = json.load(f)

        vacancies = [Vacancy(v) for v in all_vacancies]
        return vacancies

    @staticmethod
    def sort_by_salary_from(data_vacancies: list) -> list:
        """Возвращает список топ отсортированных экземпляров класса Vacancy по минимальной зарплате.
        Экземпляры где не указана минимальная зарплата перемещаются в конец списка"""
        # data_vacancies = self.choose_all()
        v_without_salary = [v for v in data_vacancies if isinstance(v.salary_from, str)]
        v_with_salary = [v for v in data_vacancies if isinstance(v.salary_from, int)]
        sorted_vacancies = sorted(v_with_salary, reverse=True)
        sorted_vacancies.extend(v_without_salary)
        return sorted_vacancies

    @staticmethod
    def sort_by_salary_to(data_vacancies: list) -> list:
        """Возвращает список топ отсортированных экземпляров класса Vacancy по максимальной зарплате.
        Экземпляры где не указана максимальная зарплата перемещаются в конец списка"""
        # data_vacancies = self.choose_all()
        v_without_salary = [v for v in data_vacancies if isinstance(v.salary_to, str)]
        v_with_salary = [v for v in data_vacancies if isinstance(v.salary_to, int)]
        sorted_vacancies = sorted(v_with_salary, key=lambda x: x.salary_to, reverse=True)
        sorted_vacancies.extend(v_without_salary)
        return sorted_vacancies

    @staticmethod
    def get_vacs_by_salary_range(data_vacancies: list, salary_range: str):
        """Возвращает список вакансий из заданного диапазона зарплаты"""
        range_list = salary_range.split("-")

        if len(range_list) != 2:
            print("Не корректный ввод")
            return

        for num in range_list:
            if num.isalpha() or num == "":
                print("Не корректный ввод")
                return

        min_r = int(range_list[0])
        max_r = int(range_list[1])
        filtered_vacancies = []

        for v in data_vacancies:
            if isinstance(v.salary_from, int) and isinstance(v.salary_to, int):
                if (v.salary_from <= min_r <= v.salary_to) or (v.salary_from <= max_r <= v.salary_to):
                    filtered_vacancies.append(v)

        return filtered_vacancies

    @staticmethod
    def get_vacancies_by_city(data_vacancies: list, city_input: str) -> list:
        """Возвращает вакансии по указанному городу"""
        v_in_city = []

        for v in data_vacancies:
            if v.city is not None:
                if v.city.lower() == city_input.lower():
                    v_in_city.append(v)

        return v_in_city

    @staticmethod
    def filter_words(data_vacancies: list, keywords: str) -> list:
        """Возвращает список вакансий где встречаются ключевые слова.
        Ключевые слова записаны через пробел."""
        filtered_vacancies = []
        keywords_list = keywords.lower().split()

        for keyword in keywords_list:
            for v in data_vacancies:
                if v.name:
                    if keyword in v.name.lower():
                        filtered_vacancies.append(v)
                elif v.requirement:
                    if keyword in v.requirement.lower():
                        filtered_vacancies.append(v)

        return filtered_vacancies
