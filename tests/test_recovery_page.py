import allure

from test_data import PageUrls
from pages.main_page import MainPage
from pages.recovery_page import RecoveryPage
from pages.login_page import LoginPage
from helpers.user_data import generate_user_data


class TestRecoveryPage:

    @allure.title('Переходим на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_recover_password_but(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page = LoginPage(driver)
        main_page.click_on_personal_account_button_mainpage()
        login_page.click_on_recovery_button()
        assert recovery_page.check_recovery_form()
        assert recovery_page.get_current_url() == PageUrls.RECOVERY_URL

    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    def test_email_input_and_click_on_recover_but(self, driver):
        main_page = MainPage(driver)
        recovery_page = RecoveryPage(driver)
        login_page = LoginPage(driver)
        main_page.click_on_personal_account_button_mainpage()
        login_page.click_on_recovery_button()
        recovery_page.send_keys_to_email_field(generate_user_data()['email'])
        recovery_page.click_on_recovery_button()
        assert recovery_page.save_button_check()
        assert recovery_page.get_current_url() == PageUrls.RESET_PASSWORD_URL

    @allure.title('Проверяем что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_click_on_password_field(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_page = RecoveryPage(driver)
        user_data = generate_user_data()
        main_page.click_on_personal_account_button_mainpage()
        login_page.click_on_recovery_button()
        recovery_page.send_keys_to_email_field(user_data['email'])
        recovery_page.click_on_recovery_button()
        assert recovery_page.check_field_password_is_active(user_data['password'])
