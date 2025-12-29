from unittest.mock import patch

from src.utils import list_to_object_vacancies, write_json_file, write_excel_file
from src.work_file import JSONWorker, XLSXWorker


def test_list_to_object_vacancies(fixture_return_API) -> None:
    result = list_to_object_vacancies(fixture_return_API)
    assert result[0].id == '128754739'


@patch("src.utils.JSONWorker.read_vacancies")
@patch("src.utils.JSONWorker.add_vacancies")
def test_write_json_file(mock_add_vacancies, mock_read_vacancies, fixture_json_file) -> None:
    """
    Тест записи в JSON-файл
    """
    json_file = JSONWorker('test_vacancies.json')
    mock_read_vacancies.return_value = fixture_json_file
    write_json_file(fixture_json_file)
    mock_add_vacancies.assert_called_once_with(fixture_json_file)


@patch("src.utils.JSONWorker.read_vacancies")
@patch("src.utils.JSONWorker.add_vacancies")
def test_write_json_file_no_data(mock_add_vacancies, mock_read_vacancies, fixture_json_file) -> None:
    """
    Тест записи в JSON-файл при отсутстии при отсутствии данных в файле
    """
    json_file = JSONWorker('test_vacancies.json')
    mock_read_vacancies.return_value = []
    write_json_file(fixture_json_file)
    mock_add_vacancies.assert_called_once_with(fixture_json_file)


@patch("src.utils.XLSXWorker.read_vacancies")
def test_write_excel_file(mock_read_vacancies, fixture_excel_file) -> None:
    """
    Тест записи в EXCEL-файл
    """
    excel_file = XLSXWorker('test_vacancies.xlsx')
    mock_read_vacancies.return_value = fixture_excel_file
    write_excel_file(fixture_excel_file)
    read_data = excel_file.read_vacancies()
    assert read_data == fixture_excel_file


@patch("src.utils.XLSXWorker.read_vacancies")
@patch("src.utils.XLSXWorker.add_vacancies")
def test_write_excel_file_no_data(mock_add_vacancies, mock_read_vacancies, fixture_excel_file) -> None:
    """
    Тест записи в EXCEL-файл при отсутсвии данных в файле
    """
    excel_file = XLSXWorker('test_vacancies.xlsx')
    mock_read_vacancies.return_value = []
    write_excel_file(fixture_excel_file)
    mock_add_vacancies.assert_called_once_with(fixture_excel_file)
