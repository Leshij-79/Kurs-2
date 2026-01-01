from src.utils import list_to_object_vacancies
from src.vacancies import Vacancy


def test_cast_to_object_list(fixture_return_API, fixture_json_file) -> None:
    """
    Тест формирования списка вакансий в формате список словарей из списка объектов Vacancy для записи в файл
    """
    result = Vacancy.cast_to_object_list(list_to_object_vacancies(fixture_return_API))
    assert result == fixture_json_file
