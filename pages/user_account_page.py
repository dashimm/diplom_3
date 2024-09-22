from locators.locators import PersonalAccountLocators
from pages.base_page import BasePage


class UserAccountPage(BasePage):
    def click_on_orders_history_button(self):
        self.click_on_element(PersonalAccountLocators.order_history_button)

    def click_on_exit_button(self):
        self.click_on_element(PersonalAccountLocators.exit_button)

    def check_order_history_form(self):
        return self.check_element(PersonalAccountLocators.order_history_form)

    def check_personal_profile_visible(self):
        return self.check_element(PersonalAccountLocators.profile_form)
