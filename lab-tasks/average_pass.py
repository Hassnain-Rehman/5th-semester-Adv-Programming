m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))

average = (m1 + m2 + m3) / 3
print(f"Average: {average:.2f}")

if average >= 50:
    print("Pass")