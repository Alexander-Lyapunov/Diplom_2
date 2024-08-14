import allure
import pytest
import requests
from helpers import *
from data import Urls


@pytest.fixture
@allure.title('Создаем пользователя и удаляем его после теста')
def create_user():
    response, login_pass, token = create_new_user()
    yield response, login_pass, token
    requests.delete(Urls.USER_URL, headers={'Authorization': f'{token}'})
