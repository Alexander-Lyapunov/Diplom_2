import allure
import pytest
import requests
from conftest import create_user
from data import Urls, Errors, StatusCode
from helpers import generate_random_string


class TestUserUpdate:
    @allure.title('Успешное изменение имени пользователя с авторизацией')
    def test_update_user_name_with_auth_success(self, create_user):
        user = create_user
        new_name = generate_random_string(5)
        update_user_data = {
            "name": new_name
        }
        token = {'Authorization': user[2]}
        response = requests.patch(Urls.USER_URL, headers=token, data=update_user_data)
        assert response.json()['success'] == True and response.json()['user']['email'] == user[1][0] and response.json()['user']['name'] == new_name

    @allure.title('Успешное изменение емейла пользователя с авторизацией')
    def test_update_user_email_with_auth_success(self, create_user):
        user = create_user
        new_email = f'{generate_random_string(10)}@yandex.ru'
        update_user_data = {
            "email": new_email
        }
        token = {'Authorization': user[2]}
        response = requests.patch(Urls.USER_URL, headers=token, data=update_user_data)
        assert response.json()['success'] == True and response.json()['user']['email'] == new_email

    @allure.title('Успешное изменение пароля пользователя с авторизацией')
    def test_update_user_password_with_auth_success(self, create_user):
        user = create_user
        new_password = generate_random_string(10)
        update_user_data = {
            "password": new_password
        }
        token = {'Authorization': user[2]}
        response = requests.patch(Urls.USER_URL, headers=token, data=update_user_data)
        assert response.json()['success'] == True and response.json()['user']['email'] == user[1][0] and response.json()['user']['name'] == user[1][2]

    @allure.title('Изменение данных пользователя без авторизации')
    @pytest.mark.parametrize("update_user_data", [
        {'email': f'{generate_random_string(10)}@yandex.ru'},
        {'password': generate_random_string(10)},
        {'name': generate_random_string(5)}
    ])
    def test_update_user_data_without_auth_fail(self, update_user_data):
        response = requests.patch(Urls.USER_URL, data=update_user_data)
        assert response.status_code == StatusCode.UNAUTHORIZED and response.json()['message'] == Errors.ERROR_NO_AUTH

