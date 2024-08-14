import requests
import random
import string
from data import Urls, StatusCode


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def create_new_user():
    login_pass = []
    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(5)
    payload = {
        "email": email,
        "password": password,
        "name": name
        }
    response = requests.post(Urls.SIGNUP_URL, data=payload)
    if response.status_code == StatusCode.OK:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)
        token = response.json()['accessToken']
    return response, login_pass, token

def get_random_user_wrong_data():
    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(5)
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(Urls.SIGNUP_URL, data=payload)
    return response