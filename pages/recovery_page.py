from pages.base_page import BasePage
from locators.locators import RecoverPageLocators


class RecoveryPage(BasePage):
    def check_recovery_form(self):
        return self.check_element(RecoverPageLocators.recover_form_text)

    def send_keys_to_email_field(self, email):
        self.send_keys_to_field(RecoverPageLocators.email_input_field, email)

    def send_keys_to_password_field(self, password):
        self.send_keys_to_field(RecoverPageLocators.new_password_input_field, password)

    def click_on_recovery_button(self):
        self.click_on_element(RecoverPageLocators.recover_button)

    def save_button_check(self):
        return self.check_element(RecoverPageLocators.save_button)

    def check_field_password_is_active(self, password):
        self.send_keys_to_password_field(password)
        self.click_on_element(RecoverPageLocators.show_password_button)
        return self.check_element(RecoverPageLocators.password_input_field_active)
