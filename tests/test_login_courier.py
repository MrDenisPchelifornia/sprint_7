import allure
import data
import base
from work_with_handlers import WorkWithHandlers
from conftest import courier_login_generate


class TestLoginCourier:
    @allure.title('Проверка факта логина, что возвращает код 200 и id вернулся')
    def test_success_login(self):
        response = WorkWithHandlers.login_courier(data.DataForLoginCourier.data_for_login_courier)
        response_id = response.json()["id"]

        assert response.status_code == 200 and response_id is not None and response_id > 0

    @allure.title('Проверка возврата ошибки 400 при поптыке игнорирования заполнения обязательного поля')
    def test_empty_password_login(self):
        data_set = base.ChangeDataForLoginCourier.change_data_for_login_courier(self, "password", "")
        logged_in_courier_request = WorkWithHandlers.login_courier(data_set)

        assert (logged_in_courier_request.status_code == 400 and logged_in_courier_request.json()['message'] ==
                data.ResponseMessages.fail_with_empty_field_for_login)

    @allure.title('Проверка возврата ошибки 404 при попытке логина с неверным паролем')
    def test_wrong_password_login(self):
        data_set = base.ChangeDataForLoginCourier.change_data_for_login_courier(self, "password", "9999")
        logged_in_courier_request = WorkWithHandlers.login_courier(data_set)

        assert (logged_in_courier_request.status_code == 404 and logged_in_courier_request.json()['message'] ==
                data.ResponseMessages.fail_with_wrong_data_for_login)

    @allure.title('Проверка ошибки 404 при попытке залогинется несуществующим курьером')
    def test_not_existed_courier_login(self, courier_login_generate):
        not_existed_courier = courier_login_generate

        assert (not_existed_courier.status_code == 404 and not_existed_courier.json()['message'] ==
                data.ResponseMessages.fail_with_wrong_data_for_login)