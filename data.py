class DataForCourierCreate:
    data_for_courier_create = {
        "login": "Sam",
        "password": "4321",
        "firstName": "Winchester"
    }

class DataForLoginCourier:
    data_for_login_courier = {
        "login": "Din",
        "password": "1234"
    }

class ResponseMessages:
    fail_with_double_account = "Этот логин уже используется. Попробуйте другой."
    fail_with_empty_field_for_creating = "Недостаточно данных для создания учетной записи"
    fail_with_empty_field_for_login = "Недостаточно данных для входа"
    fail_with_wrong_data_for_login = "Учетная запись не найдена"