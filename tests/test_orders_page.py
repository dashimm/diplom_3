import pytest
import allure

from pages.main_page import HeaderMainPage
from pages.orders_page import OrderFeedPage
from helpers.helpers_methods import Order
from locators.locators import OrderFeedLocators


class TestOrderFeedPage:

    @allure.title('Проверяем, что при клике на заказ, появляется всплывающее окно')
    def test_check_info_popup_window(self, driver):
        header = HeaderMainPage(driver)
        feed_order = OrderFeedPage(driver)
        header.click_on_order_feed_button_in_header()
        feed_order.click_on_order()
        assert feed_order.check_order_info()

    @allure.title('Проверяем что создании нового заказа счётчик за сегодня и за всё время увеличивается')
    @pytest.mark.parametrize('counter', [OrderFeedLocators.counter_of_daily_orders,
                                         OrderFeedLocators.counter_of_total_orders])
    def test_order_counter(self, driver, create_user, login_user, counter):
        order = Order()
        feed_order = OrderFeedPage(driver)
        header = HeaderMainPage(driver)
        header.click_on_order_feed_button_in_header()
        counter_before = int(feed_order.check_orders_counter(counter))
        order.create_order(create_user)
        counter_after = int(feed_order.check_orders_counter(counter))
        assert counter_after > counter_before

    @allure.title('Проверяем что после оформления заказа его номер появляется в разделе В работе')
    def test_check_order_by_user_in_progress(self, driver, create_user, login_user):
        order = Order()
        header = HeaderMainPage(driver)
        order_feed = OrderFeedPage(driver)
        header.click_on_order_feed_button_in_header()
        order.create_order(create_user)
        orders_in_progress = order_feed.get_orders_in_progress()
        user_order = str(order.get_user_orders(create_user))
        assert user_order in orders_in_progress

    @allure.title('Проверяем что заказы пользователя из раздела «История заказов» отображаются на странице «Лента '
                  'заказов»')
    def test_check_order_by_user_appears_in_history(self, driver, create_user, create_new_order, login_user):
        order = Order()
        feed_order = OrderFeedPage(driver)
        header = HeaderMainPage(driver)
        header.click_on_order_feed_button_in_header()
        user_order = str(order.get_user_orders(create_user))
        history_of_orders = feed_order.get_history_of_orders()
        assert user_order in history_of_orders
