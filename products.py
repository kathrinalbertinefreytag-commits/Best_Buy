class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name may not be empty")
        if price < 0:
            raise ValueError("Price may not be negative")
        if quantity < 0:
            raise ValueError("Quantity may not be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def activate(self):
       self.active = True


    def deactivate(self):
        self.active = False


    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity may not be negative")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        return self.active

    def show(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        if not self.active:
            raise Exception("Product is not active")

        if quantity > self.quantity:
            raise Exception("Not enough items in stock")

        self.quantity -= quantity
        bill = self.price * quantity

        if self.quantity == 0:
            self.deactivate()

        return bill






