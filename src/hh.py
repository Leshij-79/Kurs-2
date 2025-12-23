from abc import abstractmethod, ABC

import requests


class AbstraktHH(ABC):

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HeadHunterAPI(AbstraktHH):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 10, 'search_field': 'name', 'area': '3', 'period': 14,
                       'salary': 120000, 'only_with_salary': True}
        self.__vacancies = []

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 2:
            try:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            except Exception as e:
                print(f'Проверьте соединение. Ошибка - {e}')
                return self.__vacancies
            if response.status_code == 200:
                vacancies = response.json()['items']
                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
            else:
                print(f'Ошибка подключения - {response.status_code}')
                break
        return self.__vacancies


if __name__ == '__main__':
    hh1 = HeadHunterAPI()
    vak = hh1.load_vacancies('Python-разработчик')
    if len(vak) == 0:
        print('Список пуст')
    for item in vak:
        print(item)