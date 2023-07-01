from classes.websites_api import HeadHunterAPI, SuperJobAPI
import json

if __name__ == '__main__':

    while True:

        platforms = []
        vacancies = []

        use_api = input("Выберите из какого API вы хотите получить вакансии:\n"
                        "\n 1 - hh.ru\n 2 - SuperJob\n 3 - использовать оба\n\n")

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

        count_page = input("Укажите число страниц с вакансиями (максимально 5). На странице содержится 100 вакансий.\n"
                           "(Если вы выбрали оба API, то с КАЖДОГО API вернется столько страниц сколько указанно.)\n")

        if count_page.lower() == "exit":
            break
        elif (int(count_page) > 10) or (int(count_page) < 1):
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
        for i in range(200):
            # if vacancies[i]["currency"] not in ["RUB"]:
            print(json.dumps(vacancies[i], indent=2, ensure_ascii=False))
            print("-" * 30)
        break
