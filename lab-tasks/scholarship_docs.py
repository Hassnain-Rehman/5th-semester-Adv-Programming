gpa = float(input("GPA: "))
income = float(input("Monthly family income: "))

if gpa >= 3.0:
    if income <= 80000:
        docs = input("Are documents complete? (yes/no): ")
        if docs == "yes":
            print("Application accepted")
        else:
            print("Submit missing documents")
    else:
        print("Income exceeds threshold")
else:
    print("GPA requirement not met")