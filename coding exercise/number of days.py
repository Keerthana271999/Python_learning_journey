days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = int(input("Enter a year: "))
month = int(input("Enter month number (1-12): "))

is_leap = "leap year"


def leap_year(year):
    is_leap = None
    if year % 400 == 0 and year % 100 == 0:
        is_leap = "leap year"
        print(f"{year}: {is_leap}")
    elif year % 4 == 0 and year % 100 != 0:
        is_leap = "leap year"
        print(f"{year}: leap year")
    else:
        is_leap = "not a leap year"
        print(f"{year}: leap year")


leap_year(year)
if month == 2:
    if is_leap == "leap year":
        month_days = (days[month-1])+1
    else:
        month_days = days[month-1]
else:
    month_days = days[month-1]
print(f"In month {month} it has {month_days} days")
