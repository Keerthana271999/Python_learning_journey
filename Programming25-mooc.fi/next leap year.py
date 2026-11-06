# Please write a program which asks the user for a year, and prints out the next leap year.
year = int(input("Enter a year: "))
while year > 0:
    year += 1
    if year % 400 == 0 and year % 100 == 0:
        break
    elif year % 4 == 0 and year % 100 != 0:
        break
print("next leap year: ", year)
