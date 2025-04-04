class Courier:
    COURIER_0 = (None, None, None)
    COURIER_1 = (None, "None", "None")
    COURIER_2 = ("None", None, "None")
    COURIER_3 = ("None", "None", None)
    COURIER_4 = ("None", None, None)
    COURIER_5 = (None, "None", None)
    COURIER_6 = (None, None, "None")

class AcceptOrder:
    Accept_0 = ("", "111111")
    Accept_1 = ("111111", "")
    Accept_2 = ("", "")

class LoginCourier:
    Login_0 = (None, None)
    Login_1 = ("None", None)
    Login_2 = (None, "None")

class Order:
    body_0 = \
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK"
            ]
        }
    body_1 = \
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK",
                "GREY"

            ]
        }
    body_2 = \
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "GREY"
            ]
        }
    body_3 = \
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha"
        }

class Urls:
    URL_MAIN = "http://qa-scooter.praktikum-services.ru"
    URL_CREATE_COURIER = "/api/v1/courier"
    URL_LOGIN_COURIER = "/api/v1/courier/login"
    URL_CREATE_ORDER = "/api/v1/orders"
    URL_ACCEPT_ORDER = "/api/v1/orders/accept/"
    URL_TAKE_ORDER_BY_NUMBER = "/api/v1/orders/track"
    URL_TAKE_LIST_ORDERS = "/api/v1/orders"
    URL_CANCEL_ORDER = "/api/v1/orders/cancel"
    URL_FINISH_ORDER = "/api/v1/orders/finish/:id"
    URL_DELETE_COURIER = "/api/v1/courier/"