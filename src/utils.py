import json

from src.vacancies import Vacancy
from src.work_file import JSONWorker, XLSXWorker


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
    read_data_ = data_generation(read_data, vacancies)
    json_file.add_vacancies(read_data_)
    return


def write_excel_file(vacancies):
    xlsx_file = XLSXWorker()
    read_data = xlsx_file.read_vacancies()
    if read_data == []:
        xlsx_file.add_vacancies(vacancies)
        return
    read_data_ = data_generation(read_data, vacancies)
    xlsx_file.add_vacancies(read_data_)


def data_generation(read_data, vacancies):
    temp_read_id = []
    for vacancy in read_data:
        if type(vacancy['id']) is not str:
            vacancy['id'] = str(vacancy['id'])
        temp_read_id.append(vacancy['id'])
    for vacancy in vacancies:
        if type(vacancy['id']) is not str:
            vacancy['id'] = str(vacancy['id'])
        if vacancy['id'] in temp_read_id:
            continue
        else:
            read_data.append(vacancy)
    return read_data