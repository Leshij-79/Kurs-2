import json
import os
from abc import ABC, abstractmethod


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
    """
    Класс для работы с JSON-файлом
    """

    def __init__(self, file_name: str = "vacancies.json"):
        """
        Инициализация класса JSONWorker
        :param file_name: Имя файла для сохранения данный
        """
        self.__pathfile = os.path.join(os.path.dirname(__file__), "../data", file_name)


    def read_vacancies(self) -> list[dict]:
        """
        Метод чтения данных из файла
        :return: Список словарей вакансий
        """
        try:
            with open(self.__pathfile, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            return []
        except PermissionError:
            return []
        except TypeError:
            return []

        return data


    def add_vacancies(self, vacancies: list[dict]) -> None:
        """
        Метод записи данных в файл
        :param vacancies: Список соварей вакансий
        """
        with open(self.__pathfile, "w", encoding="utf-8") as json_file:
            json.dump(vacancies, json_file, ensure_ascii=False, indent=4)


    def delete_vacancies(self, vacancies: list[dict]) -> None:
        """
        Метод удаления вакансий из файла
        :param vacancies: Список словарей вакансий
        """
        pass


class XLSXWorker(WorkingWithFile):
    """
    Класс для работы с EXCEL-файлом
    """

    def __init__(self, file_name: str = "vacancies.xlsx"):
        """
        Инициализация класса XLSXWorker
        :param file_name: Имя файла для сохранения данный
        """
        self.__pathfile = os.path.join(os.path.dirname(__file__), "../data", file_name)


    def read_vacancies(self) -> list[dict]:
        """
        Метод чтения данных из файла
        :return: Список словарей вакансий
        """
        try:
            excel_data = pd.read_excel(self.__pathfile)
            return excel_data.to_dict("records")
        except FileNotFoundError:
            return []


    def add_vacancies(self, vacancies: list[dict]) -> None:
        """
        Метод записи данных в файл
        :param vacancies: Список соварей вакансий
        """
        with pd.ExcelWriter(self.__pathfile) as writer:
            df = pd.DataFrame(vacancies)
            df.to_excel(writer, sheet_name="vacancies", index=False)


    def delete_vacancies(self, vacancies: list[dict]) -> None:
        """
        Метод удаления вакансий из файла
        :param vacancies: Список словарей вакансий
        """
        pass
