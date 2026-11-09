attendance = float(input("Attendance %: "))
fee_cleared = input("Fee cleared? yes/no: ")

if attendance >= 75:
    if fee_cleared == "yes":
        print("Eligible for exam")
    else:
        print("Clear dues first")
else:
    print("Attendance requirement not met")
    