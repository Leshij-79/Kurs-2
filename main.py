# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.hh import HeadHunterAPI
from src.vacancies import Vacancy

if __name__ == '__main__':
    # user_interaction()
    hh1 = HeadHunterAPI()
    hh_vacancies = hh1.processing_vacancies(keyword='Программист', search_field='name', period=14, salary=100000,
                               area='3', only_with_salary=True)

    # Преобразование набора данных из JSON в список объектов
    if hh_vacancies != []:
        vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    else:
        raise Exception("Вакансий нет")

    # Пример работы контструктора класса с одной вакансией
    # vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

    # Сохранение информации о вакансиях в файл
    # json_saver = JSONSaver()
    # json_saver.add_vacancy(vacancy)
    # json_saver.delete_vacancy(vacancy)


