print("bank account")
'''
Create a Bank Account class having two attributes:
Account Holder Name and Balance
and two methods:
Deposit and withdraw   Make some deposit and withdraw operations but withdraw amount can not exceed the avaliable balance  
'''


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        print(f"After depositting {self.balance} with {amount}")
        self.balance += amount
        print(
            f"you have: {self.balance}")

    def withdraw(self, amount):
        print(
            f"After withdrawing {amount} from {self.balance}")
        self.balance -= amount
        print(
            f"you have: {self.balance}")


navin = BankAccount("Navin", 10000)
navin.deposit(200000)
navin.withdraw(1000)
