import json
import os
from abc import ABC, abstractmethod
from unittest import result


class WorkingWithFile(ABC):

    @abstractmethod
    def __init__(self, pathfile):
        pass

    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def add_vacancies(self, vacancies):
        pass

    @abstractmethod
    def delete_vacancies(self, vacancies):
        pass


class JSONWorker(WorkingWithFile):

    def __init__(self):
        self.pathfile = os.path.join(os.path.dirname(__file__), "../data", "vacancies.json")


    def read_vacancies(self):
        # path_json_file = os.path.abspath(self.pathfile)
        try:
            with open(self.pathfile, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            return []
        except PermissionError:
            return []

        if len(data) == 0 or type(data) is not dict:
            return []
        else:
            return data

    def add_vacancies(self, vacancies):
        try:
            with open(self.pathfile, "a", encoding="utf-8") as json_file:
                json.dump(vacancies, json_file)

                print('!!!!!TUTA!!!!!')

        except FileNotFoundError:
            with open(self.pathfile, "w", encoding="utf-8") as json_file:
                vacancies.to_json(json_file, force_ascii=False)
                print('!!!!!SDESYA!!!!!')
                # json.dump(vacancies, json_file, ensure_ascii=False)






        # result = vacancies.dumps()
        # result.to_json(self.pathfile, force_ascii=False)

    def delete_vacancies(self, vacancies):
        pass

