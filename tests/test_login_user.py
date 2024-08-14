import pytest
import allure
import requests
import helpers
from conftest import create_user
from data import Urls, Errors, StatusCode


class TestUserLogin:
    @allure.title('Авторизация существующего пользователя')
    def test_user_login_success(self, create_user):
        data_user = {"email": create_user[1][0],
                    "password": create_user[1][1]}
        response = requests.post(Urls.SIGNIN_URL, data=data_user)
        assert response.status_code == StatusCode.OK and response.json()['success'] == True

    @allure.title("Авторизация с несуществующим паролем и логином")
    def test_login_with_wrong_password_and_login_error(self):
        data_user = helpers.get_random_user_wrong_data()
        response = requests.post(Urls.SIGNIN_URL, data=data_user)
        assert response.status_code == StatusCode.UNAUTHORIZED and response.json()["message"] == Errors.ERROR_LOGIN_EMAIL_OR_PASSWORD_INCORRECT