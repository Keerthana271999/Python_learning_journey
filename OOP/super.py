# Inheritance and super may or may not have same properties and methods
# MRO - should
# to use super and MRO - must have Inheritance
class A:
    def f1(self):
        print("A")


class B(A):
    def f2(self):
        super().f1()
        print("B")


b = B()
b.f2()
