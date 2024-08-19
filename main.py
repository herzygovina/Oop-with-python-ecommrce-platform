# main.py

from ecommerce.platform import ECommercePlatform
from ecommerce.products import Product
from ecommerce.users import User
from ecommerce.admin import Admin

# Initialize platform
platform = ECommercePlatform("MyShop")

# Create products
product1 = Product("Laptop", 999.99, 10, "P001")
product2 = Product("Smartphone", 499.99, 20, "P002")

# Admin adds products to the platform
admin = Admin("admin", "adminpass", "A001")
admin.add_product(platform, product1)
admin.add_product(platform, product2)

# User registration
user = User("john_doe", "password123", "U001")
platform.register_user(user)

# User adds products to cart and places order
user.add_to_cart(product1)
order = platform.place_order(user)

# Output
print(platform)
print(user)
print(order)