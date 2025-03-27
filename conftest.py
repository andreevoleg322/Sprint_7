import requests
import pytest
import method
from data import Order
from data import Urls



@pytest.fixture(scope='function')
def login_new_courier():
    login_pass = method.register_new_courier_and_return_login_password()
    data =\
        {
            "login": login_pass[0],
            "password": login_pass[1]
        }
    response = requests.post(Urls.URL_MAIN + Urls.URL_LOGIN_COURIER, data)
    track_id = response.json()["id"]
    yield track_id
    requests.delete(Urls.URL_MAIN + Urls.URL_DELETE_COURIER + str(response.json()["id"]))


@pytest.fixture(scope='function')
def create_order():
    response = requests.post(Urls.URL_MAIN + Urls.URL_CREATE_ORDER, json=Order.body_0)
    return response.json()["track"]