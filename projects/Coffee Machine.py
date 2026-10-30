class Coffee_machine:
    required = {
        "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 30},
        "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 50},
        "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 60}
    }
    resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

    def avialable(self):
        ingredients = Coffee_machine.required[self.drink]
        for item in ("water", "milk", "coffee"):
            if Coffee_machine.resources[item] < ingredients[item]:
                print(f"Insufficient resources: {Coffee_machine.resources}")
                return False
        return True

    def make(self):
        coin5 = int(input("enter 5rs coins: "))
        coin10 = int(input("enter 10rs coins: "))
        coin20 = int(input("enter 20rs coins: "))
        total = (5*coin5)+(5*coin10)+(5*coin20)
        ingredients = Coffee_machine.required[self.drink]
        for item in ("water", "milk", "coffee"):
            if total >= ingredients["cost"]:
                Coffee_machine.resources["money"] += ingredients["cost"]
                Coffee_machine.resources[item] -= ingredients[item]
        change = total-ingredients["cost"]
        print(f"Your drink: {self.drink} and change: {change}")

    def __init__(self, drink):
        self.drink = drink

    def choice(self):
        order = False
        while not order:
            option = input(
                "choose one (latte / espresso / cappuccino / report / off): ").lower()
            if option == "report":
                print(f"avialable resources: {Coffee_machine.resources}")
            elif option == "off":
                break
            else:
                if self.avialable():
                    self.make()
                else:
                    break
                order_again = input("wanna order again (yes / no): ").lower()
                if order_again == "no":
                    order = False
                    break


cm = Coffee_machine("latte")
cm.choice()
