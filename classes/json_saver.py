import json
from abc import ABC, abstractmethod


class FileSaver(ABC):
    """Абстрактный класс для работы с вакансиями в файлах"""

    @abstractmethod
    def create_file(self, vacancies):
        pass


class JSONSaver(FileSaver):
    """Класс для работы с вакансиями в json файле"""

    def __init__(self, file_name: str):
        self.file_name = file_name

    def create_file(self, vacancies):
        """Сохранение списка вакансий в json файл"""

        with open(f'data/{self.file_name}.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, indent=2, ensure_ascii=False)



