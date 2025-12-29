from src.vacancies import Vacancy
from src.work_file import JSONWorker, XLSXWorker


def list_to_object_vacancies(vacancies: list[dict]) -> list[Vacancy]:
    """
    Функция формирования списка объектов класса Vacancy
    :param vacancies: Список словарей с вакансиями
    :return: Список объектов класса Vacancy
    """
    list_of_vacancies = []
    for vacancy_ in vacancies:
        if vacancy_['salary'] is None:
            vacancy_['salary'] = {'from': None, 'to': None, 'currency': 'RUR', 'gross': False}
        list_of_vacancies.append(Vacancy(vacancy_['id'], vacancy_['name'], vacancy_['area'], vacancy_['salary'],
                                         vacancy_['alternate_url'], vacancy_['snippet'], vacancy_['work_format']))
    return list_of_vacancies


def write_json_file(vacancies: list[dict]) -> None:
    """
    Функция записи данных в JSON-файл
    :param vacancies: Список словарей с вакансиями
    """
    json_file = JSONWorker()
    read_data = json_file.read_vacancies()
    if read_data == []:
        json_file.add_vacancies(vacancies)
        return
    read_data_ = data_generation(read_data, vacancies)
    json_file.add_vacancies(read_data_)
    return


def write_excel_file(vacancies: list[dict]) -> None:
    """
    Функция записи данных в EXCEL-файл
    :param vacancies: Список словарей с вакансиями
    """
    xlsx_file = XLSXWorker()
    read_data = xlsx_file.read_vacancies()
    if read_data == []:
        xlsx_file.add_vacancies(vacancies)
        return
    read_data_ = data_generation(read_data, vacancies)
    xlsx_file.add_vacancies(read_data_)


def data_generation(read_data: list[dict], vacancies: list[dict]) -> list[dict]:
    """
    Функция формирования списка словарей вакансий без повторов
    :param read_data: Список словарей вакансий, прочитанный из файла
    :param vacancies: Список словарей вакансий, полученный с портала HH.RU
    :return: Список словарей вакансий для записи в файл
    """
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
