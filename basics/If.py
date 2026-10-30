#IF - CHECKS ALL THE CONDITION
number=int(input("Number (1-10): "))
if number<=5:
    print(f"{number}<=5")
if number<=10:
    print(f"{number}<=10")
    
age=int(input("Age: "))
if age>=18:
    print("Eligible to vote")