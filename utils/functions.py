from classes.websites_api import HeadHunterAPI, SuperJobAPI
from classes.json_saver import JSONSaver


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


def filtering_of_vacancies(filename: str):
    """ Функция производит фильтрацию вакансий по выбранным параметрам, печатает результат.
    :param filename - название файла указывается без расширения"""

    js = JSONSaver(filename)

    user_choice = ''

    while user_choice != "return":

        vacancies = js.choose_all()

        user_choice = input(f"Введите через пробел интересующие номера для фильтрации вакансий:\n"
                            f" 1 - Сортировать вакансии по минимальной зарплате;\n"
                            f" 2 - Сортировать вакансии по максимальной зарплате;\n"
                            f" 3 - Выбрать вакансии по заданному диапазону зарплаты;\n"
                            f" 4 - Выбрать вакансии по указанному городу;\n"
                            f" 5 - Выбрать вакансии по ключевым словам;\n"
                            f"Чтобы вернуться к поиску вакансий введите 'return';\n").lower()

        if user_choice == "return":
            continue

        select_nums = user_choice.split()
        good_input = None

        for num in select_nums:
            if num.isalpha():
                good_input = False
            else:
                good_input = True

        if not good_input:
            print("\nНе корректный ввод\n")
            user_choice = ""
            continue

        for num in select_nums:
            if num == "1":
                vacancies = js.sort_by_salary_from(vacancies)

            elif num == "2":
                vacancies = js.sort_by_salary_to(vacancies)

            elif num == "3":
                input_range = input("Введите диапазон зарплаты через тире.Числа должны быть целыми!\n")

                if "-" not in input_range:
                    return ["Не корректный ввод"]

                vacancies = js.get_vacs_by_salary_range(vacancies, input_range)

                if vacancies == list():
                    print("Нет вакансий с таким диапазоном зарплат")
                    continue

            elif num == "4":
                city_input = input("Введите название города:\n")
                vacancies = js.get_vacancies_by_city(vacancies, city_input)

                if vacancies == list():
                    print("К сожалению в указанном городе нет вакансий.")
                    continue

            elif num == "5":
                input_keywords = input("Введите ключевые слова через пробел:\n")
                vacancies = js.filter_words(vacancies, input_keywords)

                if vacancies == list():
                    print("Нет вакансий, соответствующих заданным критериям.")
                    continue

        for v in vacancies:
            print(v)
        continue
