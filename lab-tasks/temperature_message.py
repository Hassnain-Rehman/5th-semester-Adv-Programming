temp = float(input("Temperature: "))

if temp >= 35:
    print("Very hot")
elif temp >= 25:
    print("Warm")
elif temp >= 15:
    print("Mild")
else:
    print("Cold")