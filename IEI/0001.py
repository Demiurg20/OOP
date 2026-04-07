n = int(input("Enter number of returned books: "))

total_fine = 0

for i in range(n):
    days = int(input(f"Enter overdue days for book {i+1}: "))

    fine = days * 15

    if days > 10:
        fine += 50

    print(f"Fine for book {i+1}: {fine} soms")

    total_fine += fine

print("Total fine for all books:", total_fine, "soms")