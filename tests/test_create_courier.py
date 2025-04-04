import pytest
import requests
import allure
import method
from data import Courier
from data import Urls

class TestCreateCourier:

    @allure.title("Ручка /api/v1/courier")
    @allure.description("Создаём курьера, используя корректные данные")
    def test_create_courier_201(self, login_new_courier):
        with allure.step('Формирование параметров курьера: логин, пароль и имя'):

            payload = \
                {
                    "login": login_new_courier[0],
                    "password": login_new_courier[1],
                    "firstName": login_new_courier[2]
                }
        with allure.step('Запрос на создание курьера'):
            response = requests.post(Urls.URL_MAIN + Urls.URL_CREATE_COURIER, data=payload)

        with allure.step('Проверки на статус и ответ'):
            assert response.status_code == 201
            assert response.json() == {'ok':True}

    @allure.title("Ручка /api/v1/courier")
    @allure.description("Создаём курьера, затем создаём ещё одного курьера, с такими же данными. Должна быть неудача.")
    def test_create_similar_couriers_error_409(self, login_new_courier):
        with allure.step('Создание нового курьера и получение его ID'):

            payload = \
                {
                    "login": login_new_courier[0],
                    "password": login_new_courier[1],
                    "firstName": login_new_courier[2]
                }
        with allure.step('Запрос на создание курьера, используя занятый логин'):
            response = requests.post(Urls.URL_MAIN + Urls.URL_CREATE_COURIER, data=payload)

        with allure.step('Проверки на статус и ответ'):
            assert response.status_code == 409
            assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Ручка /api/v1/courier")
    @allure.description("Пробуем создать курьера, комбинируя варианты заполнения обязательных полей")
    @pytest.mark.parametrize(
        "login, password, firstname",
            [
                Courier.COURIER_0,
                Courier.COURIER_1,
                Courier.COURIER_2,
                Courier.COURIER_3,
                Courier.COURIER_4,
                Courier.COURIER_5,
                Courier.COURIER_6
            ]
    )
    def test_create_courier_empty_field_error(self, login, password, firstname):

        payload = \
            {
                "login": login,
                "password": password,
                "firstName": firstname
            }
        with allure.step('Запрос на создание курьера с комбинацией заполненности полей'):
            response = requests.post(Urls.URL_MAIN + Urls.URL_CREATE_COURIER, data=payload)

        with allure.step('Проверки на статус и ответ'):
            assert response.status_code == 400
            assert response.json()["message"] == "Недостаточно данных для создания учетной записи"