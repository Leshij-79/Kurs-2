from src.utils import list_to_object_vacancies
from src.work_file import JSONWorker


def test_list_to_object_vacancies(fixture_return_API) -> None:
    result = list_to_object_vacancies(fixture_return_API)
    assert result[0].id == '128754739'


def test_write_json_file(fixture_json_file) -> None:
    json_file = JSONWorker('test_vacancies.json')
    json_file.add_vacancies(fixture_json_file)
    read_data = json_file.read_vacancies()
    assert read_data == fixture_json_file
