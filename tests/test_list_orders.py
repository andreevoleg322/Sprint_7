import requests
import allure
from data import Urls
from conftest import login_new_courier


class TestListOrders:
    @allure.title("Ручка /api/v1/orders")
    @allure.description("Получаем список заказов и смотрим количество заказов на странице")
    def test_get_list_orders_limit_10_positive(self):
        with allure.step('Запрос на список заказов и просмотр количества заказов на странице'):
            response = requests.get(Urls.URL_MAIN + Urls.URL_TAKE_LIST_ORDERS + "?limit=10&page=0")

        with allure.step('Проверки на статус и ответ'):
            assert response.status_code == 200
            assert response.json()["orders"] != []

    @allure.title("Ручка /api/v1/orders")
    @allure.description("Получаем список заказов по id курьера")
    def test_get_list_orders_by_courier_id(self, login_new_courier):
        with allure.step('Создание нового курьера и получение его ID'):
            courier_id = login_new_courier

        with allure.step('Запрос на получение списка заказов по ID курьера'):
            response = requests.get(Urls.URL_MAIN + Urls.URL_TAKE_LIST_ORDERS + "?courierId=" + str(courier_id))

        with allure.step('Проверки на статус и ответ'):
            assert response.status_code == 200
            assert response.json() is not None

    @allure.title("Ручка /api/v1/orders")
    @allure.description("Получаем список заказов и выводим значение, больше максимально требуемого")
    def test_get_list_orders_limit_100_error(self):
        with allure.step('Запрос на получение списка заказов при выводе заказов на странице 100'):
            response = requests.get(Urls.URL_MAIN + Urls.URL_TAKE_LIST_ORDERS + "?limit=100&page=0")

        with allure.step('Проверки на статус и ответ'):
            assert response.status_code == 409
            assert response.json()["message"] == "Максимальное количество заказов на странице: 30"