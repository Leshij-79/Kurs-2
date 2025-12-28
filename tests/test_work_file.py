from src.work_file import JSONWorker


def test_write_json_file(fixture_return_API) -> None:
    json_file = JSONWorker('test_vacancies.json')
    read_data = json_file.read_vacancies()
    assert read_data == fixture_return_API
