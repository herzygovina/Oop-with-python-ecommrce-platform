# ecommerce/platform.py

from ecommerce.products import Product
from ecommerce.users import User

class ECommercePlatform:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.users = []
        self.orders = []

    def register_user(self, user):
        self.users.append(user)

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, name=None, product_id=None):
        for product in self.products:
            if product.name == name or product.product_id == product_id:
                return product
        return None

    def place_order(self, user):
        order = user.checkout()
        if order:
            self.orders.append(order)
            return order
        return None

    def __str__(self):
        return f"{self.name}: Products: {[product.name for product in self.products]}, Users: {[user.username for user in self.users]}"
