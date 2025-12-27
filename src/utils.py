import json

from src.vacancies import Vacancy
from src.work_file import JSONWorker


def list_to_object_vacancies(vacancies):
    list_of_vacancies = []
    for vacancy_ in vacancies:
        print('=' * 30)
        for key, value in vacancy_.items():
            print(f'{key} === {value}')
        list_of_vacancies.append(Vacancy(vacancy_['id'], vacancy_['name'], vacancy_['area'], vacancy_['salary'],
                                         vacancy_['alternate_url'], vacancy_['snippet'], vacancy_['work_format']))
    return list_of_vacancies


def write_json_file(vacancies):
    json_file = JSONWorker()
    read_data = json_file.read_vacancies()
    if read_data == []:
        sss = json.dumps(vacancies, ensure_ascii=False)
        json_file.add_vacancies(sss)
        return
    temp_read_id = []
    for vacancy in read_data:
        temp_read_id.append(vacancy['id'])
    temp_data_for_write = []
    for vacancy in vacancies:
        if vacancy['id'] in temp_read_id:
            temp_data_for_write.append(vacancy)
    json_file.add_vacancies(json.dumps(temp_data_for_write, ensure_ascii=False))