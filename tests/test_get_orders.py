import pytest
import allure
import requests
import data
from conftest import create_user
from data import Urls, Errors, StatusCode


class TestGetOrders:
    @allure.title('Получение списка заказов пользователя с авторизацией')
    def test_get_orders_with_auth_success(self, create_user):
        token = {'Authorization': create_user[2]}
        post_order = requests.post(Urls.ORDER_URL, headers=token, data=data.Ingredients.CORRECT_INGREDIENTS)
        get_order = requests.get(Urls.ORDER_URL, headers=token)
        assert get_order.status_code == StatusCode.OK and get_order.json()['orders'][0]['number'] == post_order.json()['order']['number']

    @allure.title('Получение списка заказов пользователя без авторизации')
    def test_get_orders_without_auth_fail(self):
        post_order = requests.post(Urls.ORDER_URL, data=data.Ingredients.CORRECT_INGREDIENTS)
        get_order = requests.get(Urls.ORDER_URL)
        assert get_order.status_code == StatusCode.UNAUTHORIZED and get_order.json()['message'] == Errors.ERROR_NO_AUTH