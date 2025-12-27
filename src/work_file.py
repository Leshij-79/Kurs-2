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
                data = json.loads(json.load(json_file))
        except FileNotFoundError:
            return []
        except PermissionError:
            return []

        if len(data) == 0 or type(data) is not list:
            return []
        else:
            return data

    def add_vacancies(self, vacancies):
        with open(self.pathfile, "w", encoding="utf-8") as json_file:
            if type(vacancies) is list:
                json.dump(json.dumps(vacancies, ensure_ascii=False), json_file, ensure_ascii=False)
            else:
                json.dump(vacancies, json_file, ensure_ascii=False)



                # json.dump(vacancies, json_file, ensure_ascii=False)






        # result = vacancies.dumps()
        # result.to_json(self.pathfile, force_ascii=False)

    def delete_vacancies(self, vacancies):
        pass

