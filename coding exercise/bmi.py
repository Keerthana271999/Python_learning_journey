print("BMI calculator")
weight = int(input("Enter your weight (kg): "))
height = float(input("Enter your height (feet): "))
print(f"Your height: {height}, your weight: {weight}")
height_m = height*0.3048
bmi = weight/height_m**2
print(f"BMI = {bmi} kg/m^2")
