import allure

from test_data import PageUrls
from pages.main_page import HeaderMainPage
from pages.login_page import LoginPage
from pages.user_account_page import UserAccountPage


class TestUserAccountPage:

    @allure.title('Проверяем переход по клику на «Личный кабинет»')
    def test_go_to_user_acc(self, driver, create_user, login_user):
        header = HeaderMainPage(driver)
        personal_profile = UserAccountPage(driver)
        header.click_on_personal_profile_button_in_header()
        assert personal_profile.check_personal_profile_visible()
        assert personal_profile.get_current_url() == PageUrls.PROFILE_URL

    @allure.title('Проверяем переход в раздел «История заказов»')
    def test_go_to_orders_feed_page(self, driver, create_user, login_user):
        header = HeaderMainPage(driver)
        personal_profile = UserAccountPage(driver)
        header.click_on_personal_profile_button_in_header()
        personal_profile.click_on_orders_history_button()
        assert personal_profile.check_order_history_form()
        assert personal_profile.get_current_url() == PageUrls.ORDER_HISTORY_URL

    @allure.title('Проверяем выход из аккаунта')
    def test_exit_user_acc(self, driver, create_user, login_user):
        header = HeaderMainPage(driver)
        login_page = LoginPage(driver)
        personal_profile = UserAccountPage(driver)
        header.click_on_personal_profile_button_in_header()
        personal_profile.click_on_exit_button()
        assert login_page.check_presence_of_auth_form()
        assert login_page.get_current_url() == PageUrls.LOGIN_URL
