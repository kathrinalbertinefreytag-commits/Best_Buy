from products import Product
from store import Store

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()


product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
product_list = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(product_list[0], 1), (product_list[1], 2)]))

import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def start(store_object):
    """Main menu function. Gets a Store instance as parameter."""

    while True:
        print("\n=== Welcome to the Best Buy Store ===")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter option: ").strip()

        # 1. List all products
        if choice == "1":
            all_products = store_object.get_all_products()
            print("\n--- Products in Store ---")
            for product in all_products:
                print(product)

        # 2. Show total amount
        elif choice == "2":
            print("\nTotal quantity in store:", store_object.get_total_quantity())

        # 3. Make an order
        elif choice == "3":
            all_products = store_object.get_all_products()
            print("\n--- Available products ---")

            # Show products with index numbers
            for i, product in enumerate(all_products):
                print(f"{i}: {product}")

            order_list = []
            while True:
                index = input("\nEnter product index to buy (or 'done' to finish): ")

                if index.lower() == "done":
                    break

                if not index.isdigit() or int(index) >= len(all_products):
                    print("Invalid product number.")
                    continue

                quantity = input("Enter quantity: ")

                if not quantity.isdigit() or int(quantity) <= 0:
                    print("Invalid quantity.")
                    continue

                product = all_products[int(index)]
                order_list.append((product, int(quantity)))

            if order_list:
                try:
                    total_price = store_object.order(order_list)
                    print(f"\nOrder completed! Total cost: {total_price} dollars.")
                except Exception as e:
                    print("Error:", e)

        # 4. Quit
        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")
