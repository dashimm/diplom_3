from locators.locators import PersonalProfileLocators
from pages.base_page import BasePage


class UserAccountPage(BasePage):
    def click_on_orders_history_button(self):
        self.click_on_element(PersonalProfileLocators.order_history_button)

    def click_on_exit_button(self):
        self.click_on_element(PersonalProfileLocators.exit_button)

    def check_order_history_form(self):
        return self.check_element(PersonalProfileLocators.order_history_form)

    def check_personal_profile_visible(self):
        return self.check_element(PersonalProfileLocators.profile_form)
