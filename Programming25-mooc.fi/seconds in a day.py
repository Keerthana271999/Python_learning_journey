# write a program which asks the user for a number of days then prints out the number of seconds in the amount of days
days = int(input("Enter number of days: "))

'''
1 day = 24hr
1hr = 60min
1min = 60sec
'''

seconds = days*24*60*60
print(f"Number of seconds in {days} days: {seconds}")
