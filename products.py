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

    def get_quantity(self):
        return self.quantity

    def deactivate(selfself):
        pass

    def set_quantity(self, quantity):
        if quantity == 0:
            deactivate(self)
        return self.quantity

    def is_active(self):
        if self.quantity > 0:
            return True
        else:
            return False

    def show(self):
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity > self.quantity:
            print(f"Not enough quantity to buy. Only {self.quantity} in the shop.")
            return 0
        self.quantity -= quantity
        return self.price * quantity

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()





