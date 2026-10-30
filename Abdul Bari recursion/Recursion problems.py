# SUM OF FIRST N NATURAL NOs
def natural_no(n):
    if n == 0:
        return 0
    else:
        return natural_no(n-1)+n


print(natural_no(4))

print()

# FACTORIAL


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1)*n


print(factorial(4))
print(factorial(5))

print()

a, b = 0, 1


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)


print(fibonacci(7))

print()

i = 1


def fun1(n):
    global i
    if n >= 5:
        return n
    n = n + i
    i += 1
    return fun1(n)


print(fun1(1))

print()


def foo(n, total):
    k = 0
    j = 0
    if n == 0:
        return
    k = n % 10
    j = n // 10
    total = total + k
    foo(j, total)
    print(k)


a = 2048
total = 0
foo(a, total)
print(total)

print()


def fun(n):
    x = 1
    if n == 1:
        return x
    for k in range(1, n):
        x = x + fun(k) * fun(n - k)
    return x


print(fun(5))

print()

d = 1


def count(n):
    global d
    print(n)
    print(d)
    d += 1
    if n > 1:
        count(n - 1)
    print(d)


count(3)
