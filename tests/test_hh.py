from unittest.mock import Mock, patch

from src.hh import HeadHunterAPI


class MockResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


@patch("requests.get")
def test__AbstraktHH__load_vacancies(mock_requests_get, fixture_return_API) -> None:
    """
    Тест запроса API портала HH.RU
    """
    api_instance = HeadHunterAPI()
    mock_requests = Mock()
    mock_requests.status_code = 200
    mock_requests.json.return_value = fixture_return_API
    mock_requests_get.return_value = mock_requests
    result = api_instance._AbstraktHH__load_vacancies()
    assert result.json() == fixture_return_API


@patch("requests.get")
def test__AbstraktHH__load_vacancies_error_status_code(mock_requests_get) -> None:
    """
    Тест запроса API портала HH.RU
    """
    api_instance = HeadHunterAPI()
    mock_requests = Mock()
    mock_requests.status_code = 400
    mock_requests.json.return_value = []
    mock_requests_get.return_value = mock_requests
    result = api_instance._AbstraktHH__load_vacancies()
    assert result == []


@patch("requests.get")
def test__AbstraktHH__load_vacancies_erros_connect(mock_requests_get) -> None:
    """
    Тест ошибки отстутсвия соединения
    """
    api_instance = HeadHunterAPI()
    mock_requests = Mock()
    mock_requests_get.return_value = mock_requests
    mock_requests_get.side_effect = Exception("Connection error")
    result = api_instance._AbstraktHH__load_vacancies()
    assert result == []


@patch("src.hh.HeadHunterAPI._AbstraktHH__load_vacancies")
def test_processing_vacancies(
    mock_load_vacancies, fixture_return_API, fixture_return_API_processing_vacancies
) -> None:
    """
    Тест метода обработки вакансий при наличии API-ответа
    """
    api_instance = HeadHunterAPI()
    mock_load_vacancies.return_value = MockResponse(fixture_return_API_processing_vacancies)
    assert api_instance.processing_vacancies() == fixture_return_API


@patch("src.hh.HeadHunterAPI._AbstraktHH__load_vacancies")
def test_processing_vacancies_no_API(mock_load_vacancies) -> None:
    """
    Тест метода обработки вакансий при отсутствии API-ответа
    """
    api_instance = HeadHunterAPI()
    mock_load_vacancies.return_value = []
    assert api_instance.processing_vacancies() == []
