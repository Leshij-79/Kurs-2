import pytest


@pytest.fixture
def fixture_return_API() -> list:
    """
    Фикстура ответа на API-запрос по вакансиям
    """
    return [
        {
            "id": "128754739",
            "premium": False,
            "name": "Python Developer / Backend (парсеры)",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "3", "name": "Екатеринбург", "url": "https://api.hh.ru/areas/3"},
            "salary": {"from": 60000, "to": 160000, "currency": "RUR", "gross": False},
            "salary_range": {
                "from": 60000,
                "to": 160000,
                "currency": "RUR",
                "gross": False,
                "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                "frequency": None,
            },
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Екатеринбург",
                "street": "Восточная улица",
                "building": "7Г",
                "lat": 56.833664,
                "lng": 60.635752,
                "description": None,
                "raw": "Екатеринбург, Восточная улица, 7Г",
                "metro": None,
                "metro_stations": [],
                "id": "12818458",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-12-15T15:01:05+0300",
            "created_at": "2025-12-15T15:01:05+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=128754739",
            "show_logo_in_search": None,
            "show_contacts": True,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/128754739?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/128754739",
            "relations": [],
            "employer": {
                "id": "4306244",
                "name": "VICTORY group",
                "url": "https://api.hh.ru/employers/4306244",
                "alternate_url": "https://hh.ru/employer/4306244",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original/1462732.png",
                    "90": "https://img.hhcdn.ru/employer-logo/7470538.png",
                    "240": "https://img.hhcdn.ru/employer-logo/7470539.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=4306244",
                "country_id": 1,
                "accredited_it_employer": True,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Опыт работы с парсерами на <highlighttext>Python</highlighttext> от 1 года. "
                "Знание Playwright, selenium, Httpx, requests и подобные. Rabbit / redis "
                "приветствуются. ",
                "responsibility": "Разработка Backend микросервисов и "
                "сервисов. Проектирование новых сервисов, "
                "участие в разработке очень масштабной "
                "внутренней инфраструктуры проектов. "
                "Поддержка существующих сервисов и...",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "fly_in_fly_out_duration": [],
            "work_format": [],
            "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": False,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]


@pytest.fixture
def fixture_return_API_processing_vacancies() -> dict:
    """
    Фикстура ответа на API-запрос по вакансиям
    """
    return {
        "items": [
            {
                "id": "128754739",
                "premium": False,
                "name": "Python Developer / Backend (парсеры)",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "3", "name": "Екатеринбург", "url": "https://api.hh.ru/areas/3"},
                "salary": {"from": 60000, "to": 160000, "currency": "RUR", "gross": False},
                "salary_range": {
                    "from": 60000,
                    "to": 160000,
                    "currency": "RUR",
                    "gross": False,
                    "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                    "frequency": None,
                },
                "type": {"id": "open", "name": "Открытая"},
                "address": {
                    "city": "Екатеринбург",
                    "street": "Восточная улица",
                    "building": "7Г",
                    "lat": 56.833664,
                    "lng": 60.635752,
                    "description": None,
                    "raw": "Екатеринбург, Восточная улица, 7Г",
                    "metro": None,
                    "metro_stations": [],
                    "id": "12818458",
                },
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2025-12-15T15:01:05+0300",
                "created_at": "2025-12-15T15:01:05+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=128754739",
                "show_logo_in_search": None,
                "show_contacts": True,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/128754739?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/128754739",
                "relations": [],
                "employer": {
                    "id": "4306244",
                    "name": "VICTORY group",
                    "url": "https://api.hh.ru/employers/4306244",
                    "alternate_url": "https://hh.ru/employer/4306244",
                    "logo_urls": {
                        "original": "https://img.hhcdn.ru/employer-logo-original/1462732.png",
                        "90": "https://img.hhcdn.ru/employer-logo/7470538.png",
                        "240": "https://img.hhcdn.ru/employer-logo/7470539.png",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=4306244",
                    "country_id": 1,
                    "accredited_it_employer": True,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Опыт работы с парсерами на <highlighttext>Python</highlighttext> от 1 года. "
                    "Знание Playwright, selenium, Httpx, requests и подобные. Rabbit / redis "
                    "приветствуются. ",
                    "responsibility": "Разработка Backend микросервисов и "
                    "сервисов. Проектирование новых сервисов, "
                    "участие в разработке очень масштабной "
                    "внутренней инфраструктуры проектов. "
                    "Поддержка существующих сервисов и...",
                },
                "contacts": None,
                "schedule": {"id": "fullDay", "name": "Полный день"},
                "working_days": [],
                "working_time_intervals": [],
                "working_time_modes": [],
                "accept_temporary": False,
                "fly_in_fly_out_duration": [],
                "work_format": [],
                "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
                "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
                "night_shifts": False,
                "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
                "accept_incomplete_resumes": False,
                "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "employment_form": {"id": "FULL", "name": "Полная"},
                "internship": False,
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            }
        ]
    }


@pytest.fixture
def fixture_json_file() -> list:
    """
    Фикстура для json-файла
    :return: Список словаря вакансии
    """
    return [
        {
            "id": "128754739",
            "name": "Python Developer / Backend (парсеры)",
            "area": "Екатеринбург",
            "salary_from": 60000,
            "salary_to": 160000,
            "alternate_url": "https://hh.ru/vacancy/128754739",
            "snippet": "Опыт работы с парсерами на Python от 1 года. Знание Playwright, selenium, Httpx, requests и "
            "подобные. Rabbit / redis приветствуются.  Разработка Backend микросервисов и сервисов. "
            "Проектирование новых сервисов, участие в разработке очень масштабной внутренней "
            "инфраструктуры проектов. Поддержка существующих сервисов и...",
            "work_format": "Не определён",
        }
    ]


@pytest.fixture
def fixture_excel_file() -> list:
    """
    Фикстура для excel-файла
    :return: Список словаря вакансии
    """
    return [
        {
            "id": 128754739,
            "name": "Python Developer / Backend (парсеры)",
            "area": "Екатеринбург",
            "salary_from": 60000,
            "salary_to": 160000,
            "alternate_url": "https://hh.ru/vacancy/128754739",
            "snippet": "Опыт работы с парсерами на Python от 1 года. Знание Playwright, selenium, Httpx, requests и "
            "подобные. Rabbit / redis приветствуются.  Разработка Backend микросервисов и сервисов. "
            "Проектирование новых сервисов, участие в разработке очень масштабной внутренней "
            "инфраструктуры проектов. Поддержка существующих сервисов и...",
            "work_format": "Не определён",
        }
    ]
