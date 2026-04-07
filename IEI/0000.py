items = int(input("Enter number of items: "))

total = 0

for i in range(items):
    price = float(input(f"Enter price of item {i+1}: "))
    total += price

discount = 0

if total > 500:
    discount = total * 0.10

final_payment = total - discount

print("Total before discount:", total)
print("Discount amount:", discount)
print("Final payment:", final_payment)