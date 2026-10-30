# 12345 --> 54321
'''
divide by 10 - find remainder
find reversed number
divide the number by 10 - find new number
'''

number = int(input("Enter a number: "))

rem = rev = 0
while number != 0:
    rem = number % 10
    rev = rev*10+rem
    number //= 10
print(f"Reversed number: {rev}")
