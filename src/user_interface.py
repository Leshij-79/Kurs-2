from src.hh import HeadHunterAPI
from src.utils import list_to_object_vacancies, write_json_file, write_excel_file
from src.vacancies import Vacancy


def user_interface():
    hh1 = HeadHunterAPI()
    params = set_params()
    hh_vacancies = hh1.processing_vacancies(**params)


    if hh_vacancies == []:
        raise Exception("Вакансий нет")

    list_of_vacancies = list_to_object_vacancies(hh_vacancies)

    # print('+' * 30)
    # for item in list_of_vacancies:
    #     print(item)
    #
    # print('-' * 30)

    sorted_vacancies = sorted(list_of_vacancies, reverse=True)
    for item in sorted_vacancies[:5]:
        print(item)
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

def set_params():
    params = {'search_field': 'name'}
    keyword = input("Введите строку поиска: ")
    if keyword:
        params['keyword'] = keyword
    period = input("Введите количество дней, за которые необходим поиск: ")
    if period and period.isdigit() and int(period) > 0:
        params['period'] = int(period)
    salary = input("Введите предполагаемую зарплату (0/Enter - выводить все вакансии): ")
    if salary and salary.isdigit() and int(salary) > 0:
        params['salary'] = int(salary)
    area = input("Введите код региона поиска: ")
    if area and area.isdigit() and int(area) > 0:
        params['area'] = area
    only_with_salary = input("Показывать только с зарплатами (Д/н): ")
    if only_with_salary == "Д" or only_with_salary == "д":
        params['only_with_salary'] = True
    else:
        params['only_with_salary'] = False
    return params