from products import Product

class Store:

    def __init__(self, product_list = []):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        if product in self.product_list:
            self.product_list.remove(product)

    def get_all_products(self):
        """Returns only active products."""
        return [p for p in self.product_list if p.is_active()]

    def get_total_quantity(self):
        """Returns the sum of all product quantities."""
        return sum(p.quantity for p in self.product_list)

    def order(self, shopping_list) -> float:
        """
        shopping_list is a list of tuples: (Product, quantity)
        """
        total_order = 0.0
        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise TypeError("Each tuple must contain a Product")
            if not isinstance(quantity, int) or quantity <= 0:
                raise ValueError("Quantity must be a positive integer")


            total_order += product.buy(quantity)

        return total_order
