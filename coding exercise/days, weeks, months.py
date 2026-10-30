print("Remaining days, weeks, months calculator")
age = int(input("Enter your age (kg): "))
life_span = 90
remaining = life_span-age
days = remaining*365
weeks = remaining*52
months = remaining*12
print(f"Your age: {age}")
print(f"You have {days} days, {weeks} weeks, {months} months remaining")
