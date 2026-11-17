name = input("Student name: ")
m1 = float(input("Marks in subject 1: "))
m2 = float(input("Marks in subject 2: "))
m3 = float(input("Marks in subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("\n--- Result Card ---")
print(f"Name: {name}")
print(f"Total: {total:.2f}")
print(f"Average: {average:.2f}")

if m1 < 40 or m2 < 40 or m3 < 40:
    print("Result: Fail")
else:
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    print(f"Grade: {grade}")