name = input("Enter your name:")
surname = input("Enter your surname:")
age = int(input("Enter your age:"))
weight = int(input("Enter your weight:"))

# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.

# if ((age < 30) and ((weight > 50) or (weight < 120))):
if ((age < 30) and (50 < weight < 120)):
    print(f"You are in good condition.")
elif ((30 < age < 40) and ((weight < 50) or (weight > 120))):
    print(f"You need some training.")
elif ((age > 40) and ((weight < 50) or (weight > 120))):
    print(f"You should visit your doctor.")
else:
    print(f"Do whatever you want.")
