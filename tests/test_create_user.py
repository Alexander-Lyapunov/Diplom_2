import pytest
import allure
import requests
from conftest import create_user
from data import Urls, Errors, Data_user, StatusCode


class TestUserCreate:
    @allure.title('Успешная регистрация нового пользователя')
    def test_create_new_user_success(self, create_user):
        user = create_user[0]
        assert user.status_code == StatusCode.OK and user.json()['success'] == True

    @allure.title('Создание уже существующего пользователя')
    def test_create_exist_user_fail(self, create_user):
        exist_user = {
            "email": create_user[1][0],
            "password": create_user[1][1],
            "name": create_user[1][2]
        }
        response = requests.post(Urls.SIGNUP_URL, data=exist_user)
        assert response.status_code == StatusCode.FORBIDDEN and response.json()['success'] == False and response.json()['message'] == Errors.ERROR_CREATE_USER_ALREADY_EXIST

    @allure.title('Создание нового пользователя без заполнения обязательных полей')
    @pytest.mark.parametrize('user_data', (
            Data_user.CREATE_USER_NO_LOGIN, Data_user.CREATE_USER_NO_PASSWORD, Data_user.CREATE_USER_EMPTY_LOGIN,
            Data_user.CREATE_USER_EMPTY_PASSWORD))
    def test_create_user_without_required_fields_fail(self, user_data):
        response = requests.post(Urls.SIGNUP_URL, data=user_data)
        assert response.status_code == StatusCode.FORBIDDEN and response.json()['message'] == Errors.ERROR_CREATE_REQUIRED_FIELDS