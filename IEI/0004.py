rooms = int(input("Enter number of rooms: "))

total_usage = 0
high_usage = 0

for i in range(rooms):
    room_number = input("Enter room number: ")
    usage = float(input("Enter electricity usage (kWh): "))

    total_usage += usage

    if usage > 300:
        status = "High Usage"
        high_usage += 1
    else:
        status = "Normal Usage"

    print("Room:", room_number)
    print("Usage:", usage)
    print("Status:", status)
    print()

average = total_usage / rooms

print("Total electricity usage:", total_usage)
print("Average usage:", average)
print("Number of high usage rooms:", high_usage)