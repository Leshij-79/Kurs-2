class Vacancy():
    __slots__ = ('id', 'name', 'area', 'salary_from', 'salary_to', 'alternate_url', 'snippet', 'work_format')


    def __init__(self, id, name, area, salary, alternate_url, snippet, work_format):
        self.id = id
        self.name = name
        self.area = area['name']
        self.salary_from = self.__salary_from(salary)
        self.salary_to = self.__salary_to(salary)
        self.alternate_url = alternate_url
        self.snippet = self.__snippet(snippet)
        self.work_format = self.__work_format(work_format)


    def __salary_from(self, salary):
        if salary['from']:
            return salary['from']
        else:
            return 0


    def __salary_to(self, salary):
        if salary['to']:
            return salary['to']
        else:
            return 9999999


    def __snippet(self, snippet):
        return f'{snippet['requirement']} {snippet['responsibility']}'


    def __work_format(self, work_format):
        if work_format == []:
            return 'Не определён'
        else:
            return work_format[0]['name']


    def __lt__(self, other):
        return (self.salary_from < other.salary_from) or (self.salary_to < other.salary_to)


    def __gt__(self, other):
        return (self.salary_from > other.salary_from) or (self.salary_to > other.salary_to)


    def __eq__(self, other):
        return (self.salary_from == other.salary_from) or (self.salary_to == other.salary_to)


    def __ne__(self, other):
        return (self.salary_from != other.salary_from) or (self.salary_to != other.salary_to)


    def __le__(self, other):
        return (self.salary_from <= other.salary_from) or (self.salary_to <= other.salary_to)


    def __ge__(self, other):
        return (self.salary_from >= other.salary_from) or (self.salary_to >= other.salary_to)


    def __str__(self):
        return (f'ID вакансии - {self.id}, Вакансия - {self.name}, Территория - {self.area}, '
                f'Зарплата - {self.salary_from}-{self.salary_to}, URL вакансии - {self.alternate_url}, '
                f'Описание/требования по вакансии - {self.snippet}, Формат работы - {self.work_format}')


    # def cast_to_object_list(self, vacancies):
    def cast_to_object_list(vacancies):
        list_of_vacancies = []
        for item in vacancies:
            temp_dict = {}
            temp_dict['id'] = item.id
            temp_dict['name'] = item.name
            temp_dict['area'] = item.area
            temp_dict['salary_from'] = item.salary_from
            temp_dict['salary_to'] = item.salary_to
            temp_dict['alternate_url'] = item.alternate_url
            temp_dict['snippet'] = item.snippet
            temp_dict['work_format'] = item.work_format
            list_of_vacancies.append(temp_dict)
        return list_of_vacancies



