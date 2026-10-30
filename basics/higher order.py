'''def double(*numbers):
    """Multiply by 2"""
    for num in numbers:
        print(num*2, end=" ")


# double(1, 2, 3, 4, 5)


def square1(double, *numbers):
    double(*numbers)


square1(double, 2, 4, 6, 8, 10)'''

# Demonstrate your understanding of a Higher-Order Function by writing a Python program that takes a list of numbers and a function as input, then applies that function to each number and prints the square of each element in the list.
numbers1 = [int(num) for num in input("Enter few numbers: ").split()]


def square2():
    for num in numbers1:
        print(num**2, end=" ")


def higher_order(square2):
    square2()


higher_order(square2)
