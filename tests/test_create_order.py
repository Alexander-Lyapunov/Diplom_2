import allure
import requests
from conftest import create_user
from data import Urls, Errors, Ingredients, StatusCode


class TestCreateOrder:
    @allure.title('Создание заказа с авторизацией c ингредиентами')
    def test_create_order_with_auth_with_ingredients_success(self, create_user):
        token = {'Authorization': create_user[2]}
        post_order = requests.post(Urls.ORDER_URL, headers=token, data=Ingredients.CORRECT_INGREDIENTS)
        assert post_order.status_code == StatusCode.OK and post_order.json()['success'] == True

    @allure.title('Создание заказа с авторизацией без ингредиентов')
    def test_create_order_with_auth_without_ingredients_fail(self, create_user):
        token = {'Authorization': create_user[2]}
        post_order = requests.post(Urls.ORDER_URL, headers=token)
        assert post_order.status_code == StatusCode.BAD_REQUEST and post_order.json()['message'] == Errors.ERROR_ORDER_NO_DATA

    @allure.title('Создание заказа с авторизацией при неверном хеше ингредиентов')
    def test_create_order_with_auth_wrong_hash_fail(self, create_user):
        token = {'Authorization': create_user[2]}
        post_order = requests.post(Urls.ORDER_URL, headers=token, data=Ingredients.WRONG_INGREDIENTS)
        assert post_order.status_code == StatusCode.INTERNAL_SERVER_ERROR

    @allure.title('Создание заказа без авторизации c ингредиентами')
    def test_create_order_without_auth_success(self):
        post_order = requests.post(Urls.ORDER_URL, data=Ingredients.CORRECT_INGREDIENTS)
        assert post_order.status_code == StatusCode.OK and post_order.json()['success'] == True

    @allure.title('Создание заказа без авторизации без ингредиентов')
    def test_create_order_without_auth_without_ingredients_fail(self):
        post_order = requests.post(Urls.ORDER_URL)
        assert post_order.status_code == StatusCode.BAD_REQUEST and post_order.json()['message'] == Errors.ERROR_ORDER_NO_DATA

    @allure.title('Создание заказа без авторизации при неверном хеше ингредиентов')
    def test_create_order_without_auth_wrong_hash_fail(self):
        post_order = requests.post(Urls.ORDER_URL, data=Ingredients.WRONG_INGREDIENTS)
        assert post_order.status_code == StatusCode.INTERNAL_SERVER_ERROR


