gpa = float(input("GPA: "))
income = float(input("Monthly family income: "))

if gpa >= 3.0:
    if income <= 80000:
        print("Eligible for review")
    else:
        print("Income exceeds threshold")
else:
    print("GPA requirement not met")