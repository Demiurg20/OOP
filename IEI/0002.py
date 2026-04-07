students = int(input("Enter number of students: "))

highest = -1
lowest = 101
total = 0
passed = 0
failed = 0

for i in range(students):
    score = int(input(f"Enter score for student {i+1}: "))

    total += score

    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

    if score >= 50:
        passed += 1
    else:
        failed += 1

average = total / students

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)
print("Passed students:", passed)
print("Failed students:", failed)