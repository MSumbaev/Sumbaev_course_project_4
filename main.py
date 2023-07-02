from classes.json_saver import JSONSaver

import utils.functions as funcs


def main():
    while True:
        formatted_vacancies = []

        platforms = funcs.select_apis()

        if platforms == "exit":
            return

        select_count_v = funcs.select_count_vacancies(platforms)

        if select_count_v == "exit":
            return

        user_keyword = input("Введите ключевое слово по которому хотите найти вакансии:\n")
        print("Идет поиск вакансий...")

        for api in platforms:
            v_from_api = api.get_vacancies(user_keyword, int(select_count_v))
            formatted_vacancies.extend(api.formatted_vacancies(v_from_api))

        print(f"\nНайдено {len(formatted_vacancies)} вакансий\n")
        user_select = ''

        while user_select not in ["1", "2", "return"]:

            print(f"Чтобы продолжить выберите действие:\n "
                  f"1 - Сохранить найденные вакансии в файл {user_keyword}.json;\n "
                  f"    (ВНИМАНИЕ: Если файл с таким именем существует то он будет перезаписан)\n "
                  f"2 - Добавить найденные вакансии в файл {user_keyword}.json если он существует;\n "
                  f"    (Если такого файла нет, то он будет создан)\n "
                  f"Чтобы вернуться к поиску вакансий введите  'return'.")

            user_select = input().lower()

            if user_select not in ["1", "2", "return"]:
                print("Не корректный ввод")

        js = JSONSaver(user_keyword)
        if user_select == "return":
            continue
        elif user_select == "1":
            js.create_file(formatted_vacancies)
        elif user_select == "2":
            js.add_vacancies(formatted_vacancies)

        user_select = ''

        while user_select != "return":
            print(f"Выберите действие:\n"
                  f" 1 - Показать все вакансии;\n"
                  f" 2 - Показать топ N вакансий по минимальной зарплате;\n"
                  f" 3 - Показать топ N вакансий по максимальной зарплате;\n"
                  f" 4 - Показать вакансии по заданному диапазону зарплаты;\n"
                  f" 5 - Показать вакансии в указанном городе;\n"
                  f" 6 - Найти вакансии по ключевым словам;\n"
                  f"Чтобы очистить файл с вакансиями и вернуться к поиску введите 'clean';\n"
                  f"Чтобы вернуться к поиску вакансий введите 'return';\n"
                  f"Для выхода введите 'exit'.")

            user_select = input().lower()

            if user_select not in ["1", "2", "3", "4", "5", "6", "return", "exit", "clean"]:
                print("\nНе корректный ввод\n")
                continue

            if user_select == "exit":
                return
            elif user_select == "return":
                continue
            elif user_select == "1":
                for v in js.choose_all():
                    print(v)
            elif user_select == "2":
                for v in js.top_by_salary_from():
                    print(v)
            elif user_select == "3":
                for v in js.top_by_salary_to():
                    print(v)
            elif user_select == "4":
                salary_range = input("Введите диапазон зарплаты через дефис.\n"
                                     "Пример ввода: 1000-100000\n")
                for v in js.get_vacancies_by_salary(salary_range):
                    print(v)
            elif user_select == "5":
                city_input = input("Введите название города:\n")
                for v in js.get_vacancies_by_city(city_input):
                    print(v)
            elif user_select == "6":
                input_keywords = input("Введите ключевые слова через пробел:\n")
                for v in js.filter_words(input_keywords):
                    print(v)
            elif user_select == "clean":
                js.clean_file()
                user_select = "return"
                print("\nФайл очищен.\n")
                continue


if __name__ == '__main__':
    main()
