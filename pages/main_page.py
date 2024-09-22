from pages.base_page import BasePage
from locators.locators import MainPageLocators
from locators.locators import HeaderLocators


class HeaderMainPage(BasePage):

    def click_on_construction_button_in_header(self):
        self.click_on_element(HeaderLocators.constructor_button)

    def click_on_order_feed_button_in_header(self):
        self.click_on_element(HeaderLocators.order_feed_button)

    def click_on_personal_profile_button_in_header(self):
        self.click_on_element(HeaderLocators.personal_account_button)


class MainPage(BasePage):

    def check_constructor_form(self):
        return self.check_element(MainPageLocators.constructor_form)

    def check_order_feed_form(self):
        return self.check_element(MainPageLocators.feed_order_form)

    def click_on_personal_account_button_mainpage(self):
        self.click_on_element(MainPageLocators.personal_account_login_button)

    def click_on_bun_in_constructor(self):
        self.click_on_element(MainPageLocators.fluorescent_bun_button)

    def check_bun_info_displayed(self):
        return self.check_element(MainPageLocators.popup_from_ingredient)

    def close_info_popup(self):
        self.click_on_element(MainPageLocators.closing_cross_button)

    def check_close_bun_info(self):
        return self.check_is_element_not_visible(MainPageLocators.popup_from_ingredient)

    def wait_place_order_button_visible(self):
        self.wait_for_load_element(MainPageLocators.order_place_button)

    def check_order_form_being_displayed(self):
        return self.check_element(MainPageLocators.order_form)

    def bun_add_to_basket(self):
        self.drag_and_drop(MainPageLocators.fluorescent_bun_button, MainPageLocators.order_basket)

    def click_on_place_order_button(self):
        self.click_on_element(MainPageLocators.order_place_button)

    def get_number_of_ingredients_in_order(self):
        self.wait_for_load_element(MainPageLocators.ingredient_counter)
        return self.get_text_from_locator(MainPageLocators.ingredient_counter)

    def create_an_order(self):
        self.bun_add_to_basket()
        self.click_on_place_order_button()
