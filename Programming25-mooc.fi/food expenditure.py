# Please write a program which estimates a user's typical food expenditure.
# The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.
# Based on this information the program calculates the user's typical food expenditure both weekly and daily.

'''
price of a (a = single meal price)
you eat once = 1 day price
4 times = 4*price in a week
groceries amount is spent in a week not day. Hence, add it
'''

no_of_times = int(input("How many times you eat at the cafeteria? "))
price = float(input("Enter the price of one meal: "))
grocery = float(input("Enter the amount spent on groceries during the week: "))
weekly = (no_of_times*price)+grocery
daily = weekly/7
print(f"Daily {daily} euros.")
print(f"Weekly {weekly} euros.")
