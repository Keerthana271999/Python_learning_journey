numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))
try:
    print(f"{numerator} / {denominator}: {numerator/denominator}")
except Exception as msg:
    print(f"Exception name: {msg.__class__.__name__}")
    print(f"Error description: {msg}")
