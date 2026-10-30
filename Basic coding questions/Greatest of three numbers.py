number1=int(input("Enter 1st number: "))
number2=int(input("Enter 2nd number: "))
number3=int(input("Enter 3rd number: "))

if number1>number2 and number1>number3:
    print(f"{number1} is greater")
elif number2>number1 and number2>number3:
    print(f"{number2} is greater")
else:
    print(f"{number3} is greater")
    
