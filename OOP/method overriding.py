# Create a base class named Employee with a method calculate_salary(self) that returns a default salary amount. Create a derived class named Manager that inherits from Employee and overrides the calculate_salary(self) method to include a bonus in the calculation. Instantiate both classes, invoke their respective calculate_salary() methods, and display the outputs.
class Employee:
    def salary(self):
        print("salary: ......")


class Manager(Employee):
    def salary(self):
        print("salary + bonus: .....")


manager = Manager()
manager.salary()


class A:
    def show(self):
        print("A show")


class B(A):
    def show(self):
        print("B show")
        super().show()


obj = B()
obj.show()
