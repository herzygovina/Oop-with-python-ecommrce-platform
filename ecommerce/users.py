# ecommerce/users.py

from ecommerce.orders.cart import Cart

class User:
    def __init__(self, username, password, user_id):
        self.username = username
        self.password = password
        self.user_id = user_id
        self.cart = Cart()
        self.order_history = []

    def add_to_cart(self, product):
        if product.update_stock(1):
            self.cart.add_product(product)
            return True
        return False

    def remove_from_cart(self, product):
        if self.cart.remove_product(product):
            product.update_stock(-1)
            return True
        return False

    def checkout(self):
        if not self.cart.products:
            return False
        order = self.cart.checkout(self)
        self.order_history.append(order)
        return order

    def view_order_history(self):
        return [str(order) for order in self.order_history]

    def __str__(self):
        return f"User: {self.username}, Cart: {[product.name for product in self.cart.products]}"
