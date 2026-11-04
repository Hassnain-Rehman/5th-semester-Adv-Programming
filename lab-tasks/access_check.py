username = input("Enter username: ")
role = input("Enter role: ")

if username != "" and (role == "admin" or role == "teacher"):
    print("Access granted")
else:
    print("Access denied")