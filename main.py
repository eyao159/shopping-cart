import math


class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = quantity

    def print_item_cost(self):
        print(self.item_name, self.item_quantity,
               "@", f"${self.item_price:.1f}", "=",
               f"${self.item_price * self.item_quantity:.1f}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def get_item_pos(self, name):
        # Search the cart for an item with this name.
        for i, item in enumerate(self.cart_items):
            if name == item.item_name:
                return i
        return -1

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, name):
        i = self.get_item_pos(name)
        if i == -1:
            print("Item not found in cart. Nothing removed.")
            return
        self.cart_items.pop(i)

    def modify_item(self, item):
        i = self.get_item_pos(item.item_name)
        if i == -1:
            print("Item not found in cart. Nothing modified.")
            return
        # Only update attributes that differ from their defaults.
        if item.item_price != 0:
            self.cart_items[i].item_price = item.item_price
        if item.item_quantity != 0:
            self.cart_items[i].item_quantity = item.item_quantity

    def get_num_items_in_cart(self):
        # Add the quantities of every item in the cart.
        num_item = 0
        for item in self.cart_items:
            num_item += item.item_quantity
        return num_item

    def get_cost_of_cart(self):
        # Add each item's price multiplied by its quantity.
        cost = 0
        for item in self.cart_items:
            cost += item.item_quantity * item.item_price
        return cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        print()
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart():.1f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()


def get_quantity():
    # Ask again until the quantity is a positive whole number.
    while True:
        quantity = input("Enter the item quantity: ").strip()
        if quantity.isdecimal() and int(quantity) > 0:
            return int(quantity)
        print("Invalid quantity. Enter a positive whole number.")


def print_menu(cart):
    # Show the menu after each action until the customer quits.
    while True:
        print("\nACTIONS")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output cart description")
        print("o - Output shopping cart")
        print("q - Quit")

        choice = input("\nChoose an option: ").strip().lower()
        while choice not in ("a", "r", "c", "i", "o", "q"):
            print("Invalid option. Choose a, r, c, i, o, or q.")
            choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            break
        elif choice == "a":
            name = input("Enter the item name: ").strip()
            # Check the price text before converting it to a number.
            while True:
                price_input = input("Enter the item price: ").strip()
                if price_input.replace(".", "", 1).isdecimal():
                    price = float(price_input)
                    if math.isfinite(price):
                        break
                print("Invalid price. Enter a nonnegative number.")
            quantity = get_quantity()
            cart.add_item(ItemToPurchase(name, price, quantity))
        elif choice == "r":
            name = input("Enter name of item to remove: ").strip()
            cart.remove_item(name)
        elif choice == "c":
            name = input("Enter the item name: ").strip()
            quantity = get_quantity()
            # Change the quantity of the matching cart item.
            cart.modify_item(ItemToPurchase(name, quantity=quantity))
        elif choice == "i":
            cart.print_descriptions()
        elif choice == "o":
            cart.print_total()


def main():
    customer_name = input("Enter customer's name: ").strip()
    current_date = input("Enter today's date: ").strip()
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")
    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

if __name__ == "__main__":
    main()
