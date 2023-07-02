from classes.websites_api import HeadHunterAPI, SuperJobAPI


def select_apis():
    """Запрашивает у пользователя какие API использовать, и возвращает список экземпляров выбранных API"""
    platforms = []

    while platforms == list():
        use_api = input("Выберите с какой платформы вы хотите получить вакансии:"
                        "\n 1 - HeadHunter;\n 2 - SuperJob;\n 3 - Все вышеперечисленные.\n"
                        "(Чтобы выйти введите 'exit')\n")

        try:
            if use_api.lower() == "exit":
                return "exit"
            elif int(use_api) not in range(1, 4):
                print("Нет такого варианта")
                continue
            elif use_api == "1":
                hh = HeadHunterAPI()
                platforms.append(hh)
                return platforms
            elif use_api == "2":
                sj = SuperJobAPI
                platforms.append(sj)
                return platforms
            else:
                hh = HeadHunterAPI
                sj = SuperJobAPI
                platforms = [hh, sj]
                return platforms
        except ValueError:
            print("Не корректный ввод. Попробуйте еще раз.\n")
            continue


def select_count_vacancies(platforms: list):
    """Запрашивает у пользователя и возвращает выбор количества вакансий,
     исходя из переданного списка с экземплярами API"""
    count_vacancies = ""

    while count_vacancies == "":

        try:
            if len(platforms) == 1:
                count_vacancies = input("Выберите номер в соответствии с количеством вакансий:\n 1 - 100;\n 2 - 200;"
                                        "\n 3 - 300;\n 4 - 400;\n 5 - 500.\n(Чтобы выйти введите 'exit')\n")

                if count_vacancies.lower() == "exit":
                    return "exit"
                elif (int(count_vacancies) > 5) or (int(count_vacancies) < 1):
                    print("Не верно заданно число страниц")
                    count_vacancies = ""
                    continue
                else:
                    return count_vacancies

            elif len(platforms) == 2:
                count_vacancies = input("Выберите номер в соответствии с количеством вакансий:\n 1 - 200;\n 2 - 400;"
                                        "\n 3 - 600;\n 4 - 800;\n 5 - 1000.\n\nЧтобы выйти введите 'exit'\n")

                if count_vacancies.lower() == "exit":
                    return "exit"
                elif (int(count_vacancies) > 5) or (int(count_vacancies) < 1):
                    print("Не верно заданно число страниц")
                    count_vacancies = ""
                    continue
                else:
                    return count_vacancies
        except ValueError:
            print("Не корректный ввод. Попробуйте еще раз.\n")
            count_vacancies = ""
            continue
