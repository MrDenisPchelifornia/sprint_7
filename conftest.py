import allure
import pytest
from work_with_handlers import WorkWithHandlers
from base import CourierWithFakeData, LoginCourierWithFakeData


@pytest.fixture(scope='function')
@allure.step('Создание курьера с рандомными данными для регистрации')
def courier_generate():
    generate_of_courier = CourierWithFakeData.courier_fake_data_generate()
    response = WorkWithHandlers.create_courier(generate_of_courier)
    return response, generate_of_courier


@pytest.fixture(scope='function')
@allure.step('Создание курьера с рандомными данными для логина')
def courier_login_generate():
    response = WorkWithHandlers.login_courier(LoginCourierWithFakeData.courier_login_with_fake_data())
    return response