from src.hh import HeadHunterAPI
from src.utils import list_to_object_vacancies, write_json_file, write_excel_file
from src.vacancies import Vacancy


def user_interface():
    hh1 = HeadHunterAPI()
    params, top_vacancies = set_params()
    hh_vacancies = hh1.processing_vacancies(**params)


    if hh_vacancies == []:
        raise Exception("Вакансий нет")

    list_of_vacancies = list_to_object_vacancies(hh_vacancies)

    sorted_vacancies = sorted(list_of_vacancies, reverse=True)
    for item in sorted_vacancies[:top_vacancies]:
        print(item)
    list_of_vacancies = Vacancy.cast_to_object_list(list_of_vacancies)

    write_json_file(list_of_vacancies)
    write_excel_file(list_of_vacancies)

def set_params():
    params = {'search_field': 'name', 'only_with_salary': False}
    keyword = input("Введите строку поиска: ")
    if keyword:
        params['keyword'] = keyword
    period = input("Введите количество дней, за которые необходим поиск: ")
    if period and period.isdigit() and int(period) > 0:
        params['period'] = int(period)
    salary = input("Введите предполагаемую зарплату (0/Enter - выводить все вакансии): ")
    if salary and salary.isdigit() and int(salary) > 0:
        params['salary'] = int(salary)
        params['only_with_salary'] = True
    area = input("Введите код региона поиска: ")
    if area and area.isdigit() and int(area) > 0:
        params['area'] = area
    top_vacancies_ = input("Введите количество вакансий ТОП по зарплате для вывода на экран (по-умолчанию 5): ")
    if top_vacancies_ and top_vacancies_.isdigit() and int(top_vacancies_) > 0:
        top_vacancies = int(top_vacancies_)
    else:
        top_vacancies = 5

    return params, top_vacancies