#Odd or Even
number=int(input("Enter a number: "))
if number%2==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
    
match number%2:
    case 0:
        print(f"{number} is even")
    case _:
        print(f"{number} is odd")

even_odd=lambda number:"even" if number%2==0 else "odd"
print(even_odd(number))