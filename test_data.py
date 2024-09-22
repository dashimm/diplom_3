class PageUrls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = f'{MAIN_URL}/api/auth/register'
    DELETE_USER = f'{MAIN_URL}/api/auth/user'
    LOGIN = f'{MAIN_URL}/api/auth/login'
    CREATE_ORDER = f'{MAIN_URL}/api/orders'
    GET_ORDERS = f'{MAIN_URL}/api/orders'
    FEED_URL = f'{MAIN_URL}/feed'
    REGISTER_URL = f'{MAIN_URL}/register'
    LOGIN_URL = f'{MAIN_URL}/login'
    RECOVERY_URL = f'{MAIN_URL}/forgot-password'
    PROFILE_URL = f'{MAIN_URL}/account/profile'
    ORDER_HISTORY_URL = f'{MAIN_URL}/account/order-history'
    RESET_PASSWORD_URL = f'{MAIN_URL}/reset-password'


class Ingredients:
    valid_hash = {"ingredients": ["61c0c5a71d1f82001bdaaa6d"]}
