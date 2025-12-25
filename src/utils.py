from src.vacancies import Vacancy


def list_to_object_vacancies(vacancies):
    list_of_vacancies = []
    for vacancy_ in vacancies:
        print('=' * 30)
        for key, value in vacancy_.items():
            print(f'{key} === {value}')
        list_of_vacancies.append(Vacancy(vacancy_['id'], vacancy_['name'], vacancy_['area'], vacancy_['salary'],
                                         vacancy_['alternate_url'], vacancy_['snippet'], vacancy_['work_format']))
    return list_of_vacancies

