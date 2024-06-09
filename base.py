import allure
import requests
from faker import Faker
import data
import url_and_handle

class CourierWithFakeData:

    @staticmethod
    @allure.step('Генерация данных для регистрации курьера')
    def courier_fake_data_generate():
        fake = Faker()

        return {
            "login": fake.name(),
            "password": fake.password(),
            "firstName": fake.first_name()
        }

class ChangeDataForCourier:
    @staticmethod
    @allure.step('Генерация данных для регистрации курьера с возмождностью подмены значений')
    def change_data_for_courier(self, key, value):
        body = data.DataForCourierCreate.data_for_courier_create.copy()
        body[key] = value

        return body


class LoginCourierWithFakeData:

    @staticmethod
    @allure.step('Генерация данных для логина курьера')
    def courier_login_with_fake_data():
        fake = Faker()

        return {
            "login": fake.name(),
            "password": fake.password()
        }


class ChangeDataForLoginCourier:
    @staticmethod
    @allure.step('Генерация данных для логина курьера с возмождностью подмены значений')
    def change_data_for_login_courier(self, key, value):
        body = data.DataForLoginCourier.data_for_login_courier.copy()
        body[key] = value

        return body


class DataForDeleteCourier:
    @staticmethod
    @allure.step('Удаляем курьера')
    def data_for_delete_courier(login, password):
        response = requests.post(url_and_handle.URL + url_and_handle.courier_login, data={
            "login": login,
            "password": password,
        })
        requests.delete(url_and_handle.URL + url_and_handle.courier_delete + f"/{response.json()["id"]}")

        return response