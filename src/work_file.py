import json
import os
from abc import ABC, abstractmethod
from unittest import result

import pandas as pd


class WorkingWithFile(ABC):

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
        except TypeError:
            return []

        return data


    def add_vacancies(self, vacancies):
        with open(self.pathfile, "w", encoding="utf-8") as json_file:
            if type(vacancies) is list:
                json.dump(json.dumps(vacancies, ensure_ascii=False), json_file, ensure_ascii=False)
            else:
                json.dump(vacancies, json_file, ensure_ascii=False)


    def delete_vacancies(self, vacancies):
        pass


class XLSXWorker(WorkingWithFile):


    def __init__(self):
        self.pathfile = os.path.join(os.path.dirname(__file__), "../data", "vacancies.xlsx")


    def read_vacancies(self):
        try:
            excel_data = pd.read_excel(self.pathfile)
            return excel_data.to_dict("records")
        except FileNotFoundError:
            return []


    def add_vacancies(self, vacancies):
        with pd.ExcelWriter(self.pathfile) as writer:
            df = pd.DataFrame(vacancies)
            df.to_excel(writer, sheet_name="vacancies", index=False)


    def delete_vacancies(self, vacancies):
        pass

