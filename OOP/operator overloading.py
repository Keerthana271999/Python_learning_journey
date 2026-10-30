#operator overloading - polymorphism (one thing many forms)

# + with numbers - adds
# + with text - concatenates
print(1+2)
print("1"+"2")

print()

# * with numbers - multiplies
# * with text - repeats
print(1*2)
print("1 "*2)

print()

#This happens becase BTS special methods like __add__,
#__sub__,__mul__,__str__ gets called which knows how to 
#add / sub ... 2 numbers by taking 2 things as parameter
#self and other

#But they don't know how to add 2 objects which is defined /
#overriden in our class (overrided built-in methods)
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def __str__(self):
        return f"{self.name}: {self.balance}"
    def __add__(self,other):
        return f"Total balance - {self.balance} + {other.balance} = {self.balance+other.balance}"
    def __gt__(self,other):
        if self.balance>other.balance:
            return f"{self.name} pay's the bill"
        else:
            return f"{other.name} pay's the bill"
navin=BankAccount("Navin",5798)
jenny=BankAccount("Jenny",847)
print(navin)
print(jenny)
print(navin+jenny)
print(navin>jenny)