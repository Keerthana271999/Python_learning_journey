import math
print(__name__)

print()


def greet():
    print(__name__)


greet()

print()

if __name__ == "__main__":
    print("Hello")
print("World")

print()


def main():
    print(__name__)


if __name__ == "__main__":
    main()

print()

print(math.__name__)
print(__name__)

print()


class Test:
    print(__name__)


print(Test.__name__)

print()


def outer():
    def inner():
        print(__name__)
    inner()


outer()

print()

print(__name__)


def func():
    __name__ = "Python"
    print(__name__)


func()
print(__name__)

print()

__name__ = "Custom"


def check():
    print(__name__)


check()
print(__name__)

print()


class Demo:
    __name__ = "Inside"


print(Demo.__name__)
print(__name__)

print()


def test():
    print(__name__)


if __name__ == "__main__":
    test()
__name__ = "Python"
print(__name__)

print()

print(__name__)


def test():
    __name__ = "Custom"
    print(__name__)


test()
print(__name__)


def test():
    print(__name__)


test()
print(__name__)


def main():
    print("Inside main:", __name__)


if __name__ == "__main__":
    main()
else:
    print("Imported")


def fun():
    print(__name__)


if __name__ == "__main__":
    fun()
else:
    print("Hello")

print("World")

__name__ = "Python"


def test():
    print(__name__)


if __name__ == "__main__":
    print("Main")
else:
    print("Not Main")

test()


def outer():
    __name__ = "Custom"

    def inner():
        print(__name__)

    inner()
    print(__name__)


outer()
print(__name__)


def outer():
    __name__ = "Custom"

    def inner():
        __name__ = "Inner"
        print(__name__)

    inner()
    print(__name__)


outer()
print(__name__)

__name__ = "Global"


def first():
    __name__ = "Local"

    def second():
        print(__name__)

    second()


first()
print(__name__)
