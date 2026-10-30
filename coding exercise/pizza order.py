print("pizza ordering")
size = input("Enter pizza size (small / medium / large): ").lower()
bill = 0
if size == "small":
    bill += 100
elif size == "medium":
    bill += 200
elif size == "large":
    bill += 300
else:
    print("Invalid size")
choice = input("Do you want toppings (yes / no): ").lower()
if choice == "yes":
    topping = input(
        "Enter the topping you want (pepperoni / extra cheese): ").lower()
    if topping == "pepperoni":
        if size == "medium" or size == "large":
            bill += 50
        else:
            bill += 30
    elif topping == "extra cheese":
        bill += 20
    else:
        print("Invalid pizza topping")
print(f"You total bill: {bill}")
