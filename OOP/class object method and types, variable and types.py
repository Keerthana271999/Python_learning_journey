#The most imp thing in OOP is an object
#To create an object we need a class
#This class act as a blueprint to create an object
#An object will have it's own properties and methods which will be defined in the class

#There are 3 types of methods and variables
#1. class method, class variables
#2. instance method, instance variables
#3. static method
#4. local variables
class Laptop:
    
    #class variable which is applicable to all the objects
    #called using class
    #Later, can be changed
    location="Nagarabhavi"
    
    #instance method - where 1st parameter is self
    #init is a special method which allows you to initialize values to the object
    #so that each object can have their own values
    #It is called automatically each time a new object is created
    
    #init - special method used to initialize values
    #__new__ - constructor that creates object BTS(behind the scene)
    def __init__(self,brand,price):
        print("object created")
        print()
        self.brand=brand
        self.price=price
    
    #generation - local variable
    def details(self,generation):
        print(f"This {self.brand} laptop is {self.price} INR and is {generation}")
        
    #classmethod - cls is the first parameter
    @classmethod
    def new_loaction_laptop(cls):
        cls.location="INDIA"
        print(f"We have branches all over {cls.location}")
    
    #staticmethod - no 1st parameter
    #part of class but not related
    #called using class
    @staticmethod
    def timing():
        print("Monday - Saturday: 9:00AM - 9:00PM")
        print("Sunday: HOLIDAY")
hp=Laptop("HP",123456789)
hp.details("i9")
hp.new_loaction_laptop()
hp.timing()

print()

dell=Laptop("DELL",112233445566778899)
dell.details("i11")
dell.new_loaction_laptop()
dell.timing()