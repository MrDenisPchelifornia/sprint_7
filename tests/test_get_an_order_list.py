import allure
from work_with_handlers import WorkWithHandlers


class TestOrderList:

    @allure.title('Проверка получения списка заказов, код 200')
    def test_get_an_order_list(self):
        order_list = WorkWithHandlers.get_order_list(self)

        assert order_list.status_code == 200