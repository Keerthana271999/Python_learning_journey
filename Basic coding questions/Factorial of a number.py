# find the factorial of a number

from math import factorial

number = int(input("Enter a number: "))

# using for loop
res = 1
for num in range(1, number+1):
    res = res*num
print(f"{number}!={res}")

# using while loop
res = 1
start = 1
while start <= number:
    res = res*start
    start += 1
print(f"{number}!={res}")

# using factorial function
print(factorial(number))

# using recurssion


def fact(number):
    if number <= 1:
        return number
    else:
        return fact(number-1)*number


print(fact(5))
