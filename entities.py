class Category:

    def __init__(self, category_id, name, description=None):
        self.id = category_id
        self.name = name
        self.description = description

    def get_products_in_category(self):
        pass


class Product:

    # Attributes: id, name, description, price, image_file, discount
    # Methods: display_products(), get_product_details()

    def __init__(self, product_id, name, price, 
        description=None, image_file=None, discount=None, 
        category=None):
        
        self.id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.image_file = image_file
        self.discount = discount
        self.category = category
    
    @staticmethod
    def display_products(products_list):
        print("Show Products List")
        print("==================")
        for product in products_list:
            print(f"{product.id}. {product.name} : {product.price}")

    def get_product_details(self):
        print(self.name)
        print(f"- Price: {self.price}")
        if self.description:
            print(f"- Description: {self.description}")
        if self.image_file:
            print(f"- Image File: {self.image_file}")
        if self.discount:
            print(f"- Discount: {self.discount}")
        if self.category:
            print(f"- Category: {self.category.name}")
