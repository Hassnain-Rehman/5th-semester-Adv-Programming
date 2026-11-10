age = int(input("Age: "))
has_id = input("Do you have ID? (yes/no): ")

if age >= 18:
    if has_id == "yes":
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Under age")