# ecommerce/admin.py

from ecommerce.users import User

class Admin(User):
    def __init__(self, username, password, user_id):
        super().__init__(username, password, user_id)

    def add_product(self, platform, product):
        platform.products.append(product)

    def remove_product(self, platform, product):
        platform.products.remove(product)

    def view_all_orders(self, platform):
        return [str(order) for order in platform.orders]

    def __str__(self):
        return f"Admin: {self.username}"
