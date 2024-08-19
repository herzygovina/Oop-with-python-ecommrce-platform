# ecommerce/orders/cart.py

from ecommerce.orders.order import Order

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            return True
        return False

    def checkout(self, user):
        order = Order(user, self.products.copy())
        self.products.clear()
        return order
