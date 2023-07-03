from classes.json_saver import JSONSaver

import utils.functions as funcs


def main():
    while True:
        formatted_vacancies = []

        # Выбираем какие использовать API
        platforms = funcs.select_apis()

        if platforms == "exit":
            return

        # Выбираем количество полученных вакансий из API
        select_count_v = funcs.select_count_vacancies(platforms)

        if select_count_v == "exit":
            return

        user_keyword = input("Введите ключевое слово по которому хотите найти вакансии:\n")
        print("Идет поиск вакансий...")

        # Выполняется запрос к API, получаем вакансии и приводим к отформатированному формату
        for api in platforms:
            v_from_api = api.get_vacancies(user_keyword, int(select_count_v))
            formatted_vacancies.extend(api.formatted_vacancies(v_from_api))

        # Вывод числа полученных вакансий
        if len(formatted_vacancies) == 0:
            print("По данному запросу вакансии не найдены")
            continue
        else:
            print(f"\nНайдено {len(formatted_vacancies)} вакансий\n")

        user_select = ''

        # Цикл по выбору работы с файлом для полученных вакансий
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

        # Запись/добавление вакансий в json-файл с именем поискового запроса либо возврат к поиску
        js = JSONSaver(user_keyword)
        if user_select == "return":
            continue
        elif user_select == "1":
            js.create_file(formatted_vacancies)
        elif user_select == "2":
            js.add_vacancies(formatted_vacancies)

        user_select = ''

        # Цикл по выбору действий с вакансиями
        while user_select != "return":
            print(f"Выберите действие:\n"
                  f" 1 - Показать все вакансии;\n"
                  f" 2 - Отфильтровать вакансии;\n"
                  f"Чтобы очистить файл с вакансиями и вернуться к поиску введите 'clean';\n"
                  f"Чтобы вернуться к поиску вакансий введите 'return';\n"
                  f"Для выхода введите 'exit'.")

            user_select = input().lower()

            if user_select not in ["1", "2", "return", "exit", "clean"]:
                print("\nНе корректный ввод\n")
                continue

            if user_select == "exit":
                return
            elif user_select == "return":
                continue
            elif user_select == "clean":
                js.clean_file()
                user_select = "return"
                print("\nФайл очищен.\n")
                continue
            elif user_select == "1":
                for v in js.choose_all():
                    print(v)
            elif user_select == "2":

                # Фильтрация вакансий по заданным критериям и их вывод в консоль
                funcs.filtering_of_vacancies(user_keyword)


if __name__ == '__main__':
    main()
