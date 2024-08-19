# ecommerce/products.py

class Product:
    def __init__(self, name, price, stock, product_id):
        self.name = name
        self.price = price
        self.stock = stock
        self.product_id = product_id

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})"
