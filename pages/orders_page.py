import allure

from locators.locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def get_history_of_orders(self):
        numbers = self.get_text(OrderFeedLocators.order_history_all)
        orders_list = []
        for number in numbers:
            order_number = number.text[2:]
            orders_list.append(order_number)
        return orders_list

    def get_orders_in_progress(self):
        numbers = self.get_text(OrderFeedLocators.counter_of_orders_in_progress)
        orders_list = []
        for number in numbers:
            order_number = number.text[1:]
            orders_list.append(order_number)
        return orders_list

    def check_orders_counter(self, locator):
        return self.get_text_from_locator(locator)

    def click_on_order(self):
        self.click_after_wait(OrderFeedLocators.order_window_info)

    def check_order_info(self):
        return self.check_element(OrderFeedLocators.orders_info)
