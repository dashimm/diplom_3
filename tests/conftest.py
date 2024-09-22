import pytest
import requests
from selenium import webdriver

from helpers import user_data
from pages.login_page import LoginPage
from pages.main_page import MainPage, HeaderMainPage
from test_data import PageUrls, Ingredients


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    global driver
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(PageUrls.MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture
def create_user():
    payload = user_data.generate_user_data()
    response = requests.post(PageUrls.CREATE_USER, data=payload)
    yield payload, response
    token = response.json()['accessToken']
    headers = {'Authorization': token}
    requests.delete(PageUrls.DELETE_USER, headers=headers)


@pytest.fixture
def login_user(driver, create_user):
    data = create_user[0]
    header_page = HeaderMainPage(driver)
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    header_page.click_on_personal_profile_button_in_header()
    login_page.authorization(data['email'], data['password'])
    main_page.wait_place_order_button_visible()


@pytest.fixture
def create_new_order(create_user):
    token = create_user[1].json()['accessToken']
    headers = {"Authorization": token}
    response = requests.post(PageUrls.CREATE_ORDER, headers=headers, data=Ingredients.valid_hash)
    return response.json()['order']['number']
