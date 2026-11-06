def main():
    items = []
    subtotal = 0

    while True:
        name = input("Add item (press Enter to finish): ").strip()
        if name == "":
            break

        price = float(input("Price per unit: "))
        quantity = int(input("Quantity: "))
        items.append(name)
        subtotal += price * quantity

    total = 0
    if(len(items) > 0):
        print("\nItems:")
        for item in items:
            print(item)

        tax_rate = float(input("Tax rate (%): "))
        tax = subtotal * tax_rate / 100
        total = subtotal + tax

        print("Subtotal:", subtotal)
        print("Tax:", tax)

    print("Total:", total)

if __name__ == "__main__":
    main()

    
