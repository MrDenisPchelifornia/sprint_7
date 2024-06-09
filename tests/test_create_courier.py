import allure
import data
import base
from conftest import courier_generate
from work_with_handlers import WorkWithHandlers
from base import DataForDeleteCourier


class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера, код 201 и проверяем что удалили за собой курьера код 200')
    def test_success_create_courier(self, courier_generate):
        created_courier_request, courier = courier_generate

        assert created_courier_request.status_code == 201 and created_courier_request.json()['ok'] == True
        delete_response = DataForDeleteCourier.data_for_delete_courier(courier['login'], courier['password'])
        assert delete_response.status_code == 200

    @allure.title('Проверка возврата ошибки на попытку дублирования курьера, код 409')
    def test_create_courier_duplicate(self):
        created_courier_request = WorkWithHandlers.create_courier(data.DataForCourierCreate.data_for_courier_create)
        created_one_more_courier_request = WorkWithHandlers.create_courier(data.DataForCourierCreate.data_for_courier_create)

        assert (created_courier_request.status_code == 409 and created_courier_request.json()['message'] ==
                data.ResponseMessages.fail_with_double_account
                and created_one_more_courier_request.status_code == 409
                and created_one_more_courier_request.json()['message'] ==
                data.ResponseMessages.fail_with_double_account)

    @allure.title('Проверка возврата ошибки если одно из полей некорректно')
    def test_empty_name_create_courier(self):
        data_set = base.ChangeDataForCourier.change_data_for_courier(self, "login", "")
        created_courier_request = WorkWithHandlers.create_courier(data_set)

        assert (created_courier_request.status_code == 400 and created_courier_request.json()['message'] ==
                data.ResponseMessages.fail_with_empty_field_for_creating)