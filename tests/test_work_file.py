from src.work_file import JSONWorker, XLSXWorker


def test_json_file(fixture_json_file) -> None:
    """
    Тест JSON-файла
    """
    json_file = JSONWorker("test_vacancies.json")
    json_file.add_vacancies(fixture_json_file)
    read_data = json_file.read_vacancies()
    assert read_data == fixture_json_file


def test_excel_read_vacancies(fixture_excel_file) -> None:
    """
    Тест чтения данных с EXCEL-файла
    """
    excel_file = XLSXWorker("test_vacancies.xlsx")
    result = excel_file.read_vacancies()
    assert result == fixture_excel_file


def test_read_json_file_file_not_found() -> None:
    """
    Тест чтения с JSON-файла при ошибочном имени файла
    """
    json_file = JSONWorker("test_vacancies1.json")
    result = json_file.read_vacancies()
    assert result == []
