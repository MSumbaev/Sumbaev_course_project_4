import json
from abc import ABC, abstractmethod
from classes.vacancy import Vacancy


class FileSaver(ABC):
    """Абстрактный класс для работы с вакансиями в файлах"""

    @abstractmethod
    def create_file(self, vacancies):
        """Сохранение списка вакансий в файл"""
        pass


class JSONSaver(FileSaver):
    """Класс для работы с вакансиями в json файле"""

    def __init__(self, file_name: str):
        self.file_name = file_name

    def create_file(self, found_vacancies):
        """Сохранение списка вакансий в json файл"""
        with open(f'data/{self.file_name}.json', 'w', encoding='utf-8') as f:
            json.dump(found_vacancies, f, indent=2, ensure_ascii=False)
        print("Файл сохранен в папку data/.")

    def add_vacancies(self, data_vacancies):
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

            print("Операция прошла успешно")

    def clean_file(self):
        """Очищает файл с вакансиями"""
        with open(f'data/{self.file_name}.json', 'w', encoding='utf-8') as f:
            f.write("")

    def choose_all(self):
        """Возвращает список всех вакансий из файла в виде экземпляра класса Vacancy()"""
        with open(f'data/{self.file_name}.json', 'r', encoding='utf-8') as f:
            all_vacancies = json.load(f)

        vacancies = [Vacancy(v) for v in all_vacancies]
        return vacancies

    def top_by_salary_from(self):
        """Возвращает список топ отсортированных экземпляров класса Vacancy по минимальной зарплате.
        Экземпляры где не указана минимальная зарплата перемещаются в конец списка"""
        data_vacancies = self.choose_all()
        v_without_salary = [v for v in data_vacancies if isinstance(v.salary_from, str)]
        v_with_salary = [v for v in data_vacancies if isinstance(v.salary_from, int)]
        sorted_vacancies = sorted(v_with_salary, reverse=True)
        sorted_vacancies.extend(v_without_salary)
        return sorted_vacancies

    def top_by_salary_to(self):
        """Возвращает список топ отсортированных экземпляров класса Vacancy по максимальной зарплате.
        Экземпляры где не указана максимальная зарплата перемещаются в конец списка"""
        data_vacancies = self.choose_all()
        v_without_salary = [v for v in data_vacancies if isinstance(v.salary_to, str)]
        v_with_salary = [v for v in data_vacancies if isinstance(v.salary_to, int)]
        sorted_vacancies = sorted(v_with_salary, key=lambda x: x.salary_to, reverse=True)
        sorted_vacancies.extend(v_without_salary)
        return sorted_vacancies

    def get_vacancies_by_salary(self, salary_range: str):
        """Возвращает список вакансий из заданного диапазона зарплаты"""
        salary_range_list = salary_range.split("-")
        data_vacancies = self.choose_all()
        filtered_v = []
        for v in data_vacancies:
            if isinstance(v.salary_from, int) and isinstance(v.salary_to, int):
                if int(salary_range_list[0]) <= v.salary_from <= int(salary_range_list[1]):
                    if int(salary_range_list[0]) <= v.salary_to <= int(salary_range_list[1]):
                        filtered_v.append(v)

        if filtered_v == list():
            return ["К сожалению нет вакансий с таким диапазоном зарплат."]
        else:
            return filtered_v

    def get_vacancies_by_city(self, city_input: str):
        """Возвращает вакансии по указанному городу"""
        data_vacancies = self.choose_all()
        v_in_city = []

        for v in data_vacancies:
            if v.city is not None:
                if v.city.lower() == city_input.lower():
                    v_in_city.append(v)

        if v_in_city == list():
            return ["К сожалению в указанном городе нет вакансий."]
        else:
            return v_in_city

    def filter_words(self, keywords: str):
        """Возвращает список вакансий где встречаются ключевые слова.
        Ключевые слова записаны через пробел."""
        filtered_vacancies = []
        data_vacancies = self.choose_all()
        keywords_list = keywords.lower().split()

        for keyword in keywords_list:
            for v in data_vacancies:
                if keyword in v.name:
                    filtered_vacancies.append(v)
                elif keyword in v.requirement:
                    filtered_vacancies.append(v)

        if filtered_vacancies == list():
            return ["Нет вакансий, соответствующих заданным критериям."]
        else:
            return filtered_vacancies
