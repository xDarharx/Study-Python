name = input("Enter your name:")
surname = input("Enter your surname:")
age = int(input("Enter your age:"))
weight = int(input("Enter your weight:"))

if ((age < 30) and (50 < weight < 120)):
    print(f"You are in good condition.")
elif ((30 < age < 40) and (50 > weight > 120)):
    print(f"You need some training.")
elif ((age > 40) and (50 > weight > 120)):
    print(f"You should visit your doctor.")
else:
    print(f"Do whatever you want.")
