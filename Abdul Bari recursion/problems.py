#Sum of 1st N natural numbers
def addition(n):
    if n==0:
        return 0
    else:
        return addition(n-1)+n
print(addition(5))
print(addition(0))
print(addition(1))

print()

#Factorial of a number
def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return factorial(number-1)*number
print(factorial(5))
print(factorial(0))
print(factorial(1))

print()

#Fibonacci series 011235
def fibonnacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonnacci(n-2)+fibonnacci(n-1)
print(fibonnacci(5))