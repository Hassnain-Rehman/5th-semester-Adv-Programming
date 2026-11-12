age = int(input("Age: "))
percentage = float(input("Percentage: "))
documents = input("Are documents complete? (yes/no): ")

if age < 17:
    print("Not eligible: minimum age is 17")
elif percentage < 60:
    print("Not eligible: minimum percentage is 60")
elif documents != "yes":
    print("Not eligible: documents are incomplete")
else:
    print("Eligible for application")