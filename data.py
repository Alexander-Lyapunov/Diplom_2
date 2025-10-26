class Urls:
    URL = 'https://stellarburgers.nomoreparties.site'
    SIGNUP_URL = URL + '/api/auth/register'
    SIGNIN_URL = URL + '/api/auth/login'
    USER_URL = URL + '/api/auth/user'
    ORDER_URL = URL + '/api/orders'

class StatusCode:
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    INTERNAL_SERVER_ERROR = 500

class Errors:
    ERROR_CREATE_USER_ALREADY_EXIST = "User already exists"
    ERROR_CREATE_REQUIRED_FIELDS = "Email, password and name are required fields"
    ERROR_LOGIN_EMAIL_OR_PASSWORD_INCORRECT = "email or password are incorrect"
    ERROR_NO_AUTH = "You should be authorised"
    ERROR_ORDER_NO_DATA = "Ingredient ids must be provided"

class Data_user:
    CREATE_USER_NO_LOGIN = {"password": "testpassword", "name": "Alexander"}
    CREATE_USER_NO_PASSWORD = {"email": "Alexander@yandex.ru", "name": "Alexander"}
    CREATE_USER_EMPTY_LOGIN = {"email": "", "password": "testpassword", "name": "Alexander"}
    CREATE_USER_EMPTY_PASSWORD = {"email": "Alexander@yandex.ru", "password": "", "name": "Alexander"}

class Ingredients:
    CORRECT_INGREDIENTS = {"ingredients":  ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa6f"]}
    WRONG_INGREDIENTS = {"ingredients":  ["aa1111aa", "bb2222bb", "cc3333cc"]}