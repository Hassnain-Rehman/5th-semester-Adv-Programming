customer_name = input("Customer name: ")
item_name = input("Item name: ")
unit_price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

subtotal = unit_price * quantity

if subtotal >= 5000:
    discount = subtotal * 0.10
else:
    discount = 0

final_total = subtotal - discount

print("\n--- Bill ---")
print(f"Customer: {customer_name}")
print(f"Item: {item_name}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final total: {final_total:.2f}")