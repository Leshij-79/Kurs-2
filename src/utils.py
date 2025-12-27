import json

from src.vacancies import Vacancy
from src.work_file import JSONWorker


def list_to_object_vacancies(vacancies):
    list_of_vacancies = []
    for vacancy_ in vacancies:
        # print('=' * 30)
        # for key, value in vacancy_.items():
        #     print(f'{key} === {value}')
        list_of_vacancies.append(Vacancy(vacancy_['id'], vacancy_['name'], vacancy_['area'], vacancy_['salary'],
                                         vacancy_['alternate_url'], vacancy_['snippet'], vacancy_['work_format']))
    return list_of_vacancies


def write_json_file(vacancies):
    json_file = JSONWorker()
    read_data = json_file.read_vacancies()
    if read_data == []:
        json_file.add_vacancies(vacancies)
        return
    temp_read_id = []
    for vacancy in read_data:
        temp_read_id.append(vacancy['id'])
    for vacancy in vacancies:
        if vacancy['id'] in temp_read_id:
            continue
        else:
            read_data.append(vacancy)

    json_file.add_vacancies(read_data)
    return
