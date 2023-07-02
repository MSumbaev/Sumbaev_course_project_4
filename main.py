from classes.websites_api import HeadHunterAPI, SuperJobAPI
import json

if __name__ == '__main__':

    while True:

        platforms = []
        vacancies = []

        use_api = input("Выберите с какой платформы вы хотите получить вакансии:"
                        "\n 1 - HeadHunter;\n 2 - SuperJob;\n 3 - Все вышеперечисленные.\n"
                        "(Чтобы выйти наберите 'exit')\n")

        if use_api.lower() == "exit":
            break
        elif int(use_api) not in range(1, 4):
            print("Нет такого варианта")
            continue
        elif int(use_api) == 1:
            hh = HeadHunterAPI()
            platforms.append(hh)
        elif int(use_api) == 2:
            sj = SuperJobAPI
            platforms.append(sj)
        else:
            hh = HeadHunterAPI
            sj = SuperJobAPI
            platforms = [hh, sj]

        count_page = ''

        if use_api in ["1", "2"]:
            count_page = input("Выберите номер в соответствии с количеством вакансий:\n 1 - 100;\n 2 - 200;"
                               "\n 3 - 300;\n 4 - 400;\n 5 - 500.\n(Чтобы выйти наберите 'exit')\n")

            if count_page.lower() == "exit":
                break
            elif (int(count_page) > 5) or (int(count_page) < 1):
                print("Не верно заданно число страниц")
                continue

        elif use_api == "3":
            count_page = input("Выберите номер в соответствии с количеством вакансий:\n 1 - 200;\n 2 - 400;"
                               "\n 3 - 600;\n 4 - 800;\n 5 - 1000.\n\nЧтобы выйти наберите 'exit'\n")

            if count_page.lower() == "exit":
                break
            elif (int(count_page) > 5) or (int(count_page) < 1):
                print("Не верно заданно число страниц")
                continue

        user_keyword = input("Введите ключевое слово по которому хотите найти вакансии:\n")

        for api in platforms:
            vac = api.get_vacancies(user_keyword, int(count_page))
            vacancies.extend(api.formatted_vacancies(vac))
            # vacancies.extend(api.get_vacancies(user_keyword, int(count_page)))

        print("количество вакансий найдено:", len(vacancies))
        print(type(vacancies))
        print(type(vacancies[0]))
        for i in range(10):
            # if vacancies[i]["currency"] not in ["RUB"]:
            print(json.dumps(vacancies[i], indent=2, ensure_ascii=False))
            print("-" * 30)
        break
