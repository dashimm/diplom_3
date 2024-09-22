import requests
from test_data import Ingredients
from test_data import PageUrls


class Order:

    def create_order(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        requests.post(PageUrls.CREATE_ORDER, headers=headers, data=Ingredients.valid_hash)

    def get_user_orders(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response = requests.get(PageUrls.GET_ORDERS, headers=headers)
        return response.json()['orders'][0]['number']
