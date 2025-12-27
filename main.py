# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.hh import HeadHunterAPI
from src.utils import list_to_object_vacancies, write_json_file, write_excel_file
from src.vacancies import Vacancy
from src.work_file import JSONWorker

if __name__ == '__main__':
    # user_interaction()
    hh1 = HeadHunterAPI()
    hh_vacancies = hh1.processing_vacancies(keyword='Python', search_field='name', period=14, salary=100000,
                               area='4', only_with_salary=True)

    # Преобразование набора данных из JSON в список объектов

    if hh_vacancies == []:
        raise Exception("Вакансий нет")

    list_of_vacancies = list_to_object_vacancies(hh_vacancies)

    # print('+' * 30)
    # for item in list_of_vacancies:
    #     print(item)
    #
    # print('-' * 30)

    sorted_vacancies = sorted(list_of_vacancies, reverse=True)
    # for item in sorted_vacancies:
    #     print(item)
    list_of_vacancies = Vacancy.cast_to_object_list(list_of_vacancies)
    # print('#' * 30)
    # for item in list_of_vacancies:
    #     print(item)

    list_of_vacancies1 = Vacancy.cast_to_object_list(sorted_vacancies)
    # print('#' * 30)
    # for item in list_of_vacancies1:
    #     print(item)

    write_json_file(list_of_vacancies)
    write_excel_file(list_of_vacancies)

    # Сохранение информации о вакансиях в файл
    # json_saver = JSONSaver()
    # json_saver.add_vacancy(vacancy)
    # json_saver.delete_vacancy(vacancy)




