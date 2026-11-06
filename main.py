class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = quantity

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, 
               "@", f"${self.item_price:.1f}", "=", 
               f"${self.item_price * self.item_quantity:.1f}")

def main():
    items = []
    subtotal = 0

    while True:
        name = input("Add item (enter 'q' to check out): ").strip()
        if name == "q":
            break

        price = float(input("Price per unit: "))
        quantity = int(input("Quantity: "))
        item = ItemToPurchase(name, price, quantity)
        items.append(item)
        subtotal += price * quantity

    # if items:
    #     tax_rate = float(input("Tax rate (%): "))

    # total = 0.0
    print("\nTOTAL COST")
    
    if items:
        for i in items:
            i.print_item_cost()

        # tax = subtotal * tax_rate / 100
        # total = subtotal + tax

        print("Total:", f"${subtotal:.1f}")
        # print("Tax:", f"${tax:.1f}")

    # print("Total (after tax):", f"${total:.1f}")

if __name__ == "__main__":
    main()

    
