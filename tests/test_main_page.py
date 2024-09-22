import allure

from test_data import PageUrls
from pages.main_page import MainPage, HeaderMainPage


class TestMainPage:

    @allure.title('Проверяем переход по клику на «Конструктор»')
    def test_click_to_constructor(self, driver):
        header = HeaderMainPage(driver)
        main_page = MainPage(driver)
        main_page.click_on_personal_account_button_mainpage()
        header.click_on_construction_button_in_header()
        assert main_page.check_constructor_form() and main_page.get_current_url() == PageUrls.MAIN_URL + '/'

    @allure.title('Проверяем переход по клику на «Лента заказов»')
    def test_click_to_order_feed(self, driver):
        header = HeaderMainPage(driver)
        main_page = MainPage(driver)
        header.click_on_order_feed_button_in_header()
        assert main_page.check_order_feed_form() and main_page.get_current_url() == PageUrls.FEED_URL

    @allure.title('Проверяем всплывающее окно при клике на ингредиент')
    def test_check_bun_info_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_in_constructor()
        assert main_page.check_bun_info_displayed()

    @allure.title('Проверяем закрытие всплывающего окна')
    def test_check_bun_info_window_closed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_in_constructor()
        main_page.close_info_popup()
        assert main_page.check_close_bun_info()

    @allure.title('Проверяем, что при добавлении ингредиента в заказ счётчик увеличивается')
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        main_page.bun_add_to_basket()
        assert int(main_page.get_number_of_ingredients_in_order()) > 0

    @allure.title('Проверяем, что залогиненный юзер может оформить заказ')
    def test_create_order_by_logged_user(self, driver, create_user, login_user):
        main_page = MainPage(driver)
        header = HeaderMainPage(driver)
        header.click_on_construction_button_in_header()
        main_page.create_an_order()
        assert main_page.check_order_form_being_displayed()
