# ecommerce/orders/order.py

class Order:
    order_counter = 0

    def __init__(self, user, items):
        self.order_id = Order.order_counter + 1
        self.user = user
        self.items = items
        self.total_amount = sum(item.price for item in items)
        self.status = "Pending"
        Order.order_counter += 1

    def update_status(self, status):
        self.status = status

    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}: {self.status}, Total: ${self.total_amount}"
