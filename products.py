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
       return True

    def deactivate(self):
        self.active = False
        return False


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        if quantity < 0:
            raise ValueError("Quantity may not be negative")


    def is_active(self):
        if self.active == True:
            return True
        else:
            return False

    def show(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        bill = 0


        if quantity <= self.quantity and quantity > 0 and self.active == True:
            self.quantity = self.quantity - quantity
            bill = self.price * quantity
            #print(f"Bill: {bill}")
            return bill
        else:
            deactivate(self)





