cars = int(input("Enter number of cars: "))

allowed = []
guests = []

for i in range(cars):
    plate = input("Enter plate number: ")
    driver = input("Enter driver type (student/teacher/guest): ")

    if driver == "student" or driver == "teacher":
        allowed.append(plate)
    else:
        guests.append(plate)

print("\nAllowed cars:")
for car in allowed:
    print(car)

print("\nGuest cars:")
for car in guests:
    print(car)

print("\nTotal allowed:", len(allowed))
print("Total guests:", len(guests))