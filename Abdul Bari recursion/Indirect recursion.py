#INDIRECT RECURSION
def func1(n):
    if n>0:
        print(n)
        func2(n-1)
def func2(n):
    if n>1:
        print(n)
        func1(n//2)
func1(20)