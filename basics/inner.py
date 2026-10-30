def outer():
    print("outer")

    def inner():
        print("inner")
    inner()


outer()

print()
# Create a Python program where a function greet() defines another function message() inside it.
# The inner function should print "Welcome to Python!".
# The outer function should call the inner one.


def greet():
    def message():
        print("welcome to python")
    message()


greet()
