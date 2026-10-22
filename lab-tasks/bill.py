item = input("Enter item name: ")
price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\n--- Bill ---")
print(f"Item: {item}")
print(f"Unit price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}")