from abc import abstractmethod, ABC

import requests


class AbstraktHH(ABC):

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


# class HH(Parser):
class HH(AbstraktHH):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    # def __init__(self, file_worker):
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 10, 'search_field': 'name', 'area': '3', 'period': 14,
                       'salary': 120000}
        self.vacancies = []
        # super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 2:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies


if __name__ == '__main__':
    hh1 = HH()
    vak = hh1.load_vacancies('Python-разработчик')
    if len(vak) == 0:
        print('Список пуст')
    for item in vak:
        print(item)