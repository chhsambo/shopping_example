from entities import Product, Category


desktop = Category(1, "Desktop")
laptop = Category(2, "Laptop")

p1 = Product(
    1, 
    "Lenovo 5400", 
    850, 
    "CPU: Core i7 RAM: 8GB...",
    category=laptop
)
p2 = Product(
    product_id=2,
    name="Dell Latitute 6500",
    price=1150
)
p3 = Product(
    product_id=3,
    name="HP 5000",
    price=540,
    category=desktop
)
p1.category = laptop
p2.category = laptop

products_list = [p1, p2, p3]


Product.display_products(products_list)

p1.get_product_details()