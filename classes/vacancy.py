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
        self.experience = vacancy["experience"]
        self.API = vacancy["API"]

    def __gt__(self, other):
        pass

    def __str__(self):
        pass
