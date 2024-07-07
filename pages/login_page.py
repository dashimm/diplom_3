from pages.base_page import BasePage
from locators.locators import AuthPageLocators


class LoginPage(BasePage):

    def send_keys_to_email_field(self, email):
        self.send_keys_to_field(AuthPageLocators.email_input_field, email)

    def send_keys_to_password_field(self, password):
        self.send_keys_to_field(AuthPageLocators.password_input_field, password)

    def click_on_login_button(self):
        self.click_on_element(AuthPageLocators.login_account_button)

    def authorization(self, email, password):
        self.send_keys_to_email_field(email)
        self.send_keys_to_password_field(password)
        self.click_on_login_button()

    def click_on_recovery_button(self):
        self.click_on_element(AuthPageLocators.recovery_button)

    def check_presence_of_auth_form(self):
        return self.check_element(AuthPageLocators.authorization_form)
