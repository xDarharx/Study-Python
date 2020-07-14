number = -1

while ((number < 0) or (number > 10)):
    number = int(input("Enter a number greater than 0, but less than 10: "))
    if ((number < 0) or (number > 10)):
        print (f"Number is wrong.")
    
print(f"Result is: {number**2}")
