import allure
import requests
import url_and_handle

class WorkWithHandlers:
    @allure.step('Создание курьера')
    def create_courier(data):
        response = requests.post(url_and_handle.URL + url_and_handle.courier_create, json=data)
        return response

    @allure.step('Логин курьера в системе')
    def login_courier(data):
        response = requests.post(url_and_handle.URL + url_and_handle.courier_login, json=data)
        return response

    @allure.step('Создание заказа')
    def create_order(data):
        response = requests.post(url_and_handle.URL + url_and_handle.order_create, json=data)
        return response

    @allure.step('Получение списка заказов')
    def get_order_list(self):
        response = requests.get(url_and_handle.URL + url_and_handle.order_list)
        return response
