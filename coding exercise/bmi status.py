print("BMI calculation and weight status")
weight = int(input("Enter your weight (kg): "))
height = float(input("Enter your height (feet): "))
height_m = height*0.3048
bmi = weight/height_m**2
print(f"Your height: {height}, your weight: {weight}")
if bmi <= 0.73:
    print(f"bmi: {bmi} kg/m^2 - underweight")
elif bmi <= 0.99:
    print(f"bmi: {bmi} kg/m^2 - normal")
elif bmi <= 1.99:
    print(f"bmi: {bmi} kg/m^2 - overweight")
else:
    print(f"bmi: {bmi} kg/m^2 - obese")
