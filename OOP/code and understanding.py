#The most important thing in OPP is an object
#To create and object we need a class
#This class act as a blueprint for whoever creates an object
#An object will have it's own properties an methods that is defined in the class
class Animal:
    #There are 3 types of variables and methods
    
    #1.class variable - applicable to all the objects and is acccessed using class name
    Zoo="Bannerghatta"
    
    #2. instance variable - applicable to specific object
    #init is a special method that is used to initialize values to each object
    #__new__ special method which creates object
    
    #i. instance method - a method where self is 1st parameter where represent current object
    def __init__(self,animal,sound):
        self.animal=animal
        self.sound=sound
    
    #3. local variable - It is applicable to that particular method        
    def animal_sound(self,category):
        print(f"The {self.animal} {self.sound}'s. It is a {category}")
       
    #classmethod - method where cls is 1st parameter which is used to work with class variable.
    #It is accessed using class name
    @classmethod
    def zoo_name(cls):
        print(f"This is {cls.Zoo} National park")
        
    #staticmethod - It is a part of class but not related which has no 1st parameter
    @staticmethod
    def timing():
        print("Monday - Sturday: 9:AM - 9:PM")
        print("Sunday: Holiday")

lion=Animal("Lion","Roar")
lion.animal_sound("Carnivorous")
Animal.zoo_name()
Animal.timing()