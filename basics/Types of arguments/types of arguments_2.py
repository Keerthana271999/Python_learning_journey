#Types of arguments
#1. positional - order matters
def greet(name,native):
    print(f"My name is {name}. I am from {native}")
greet("Keerthana","Bangalore")
greet("Bangalore","Keerthana")

print()

#2. Keyword - order does not matter
greet(name="Keerthana",native="Bangalore")
greet(native="Bangalore",name="Keerthana")

print()

#COMBO - positional and Keyword
#1st positional then Keyword
greet("Keerthana",native="Bangalore")

print()

#3. Default - always non-default arguments at 1st
#Default arguments at last
def greet(name,native="Bangalore"):
    print(f"My name is {name}. I am from {native}")
greet("Keerthana")

#positional and Default - combo
greet("Keerthana","INDIA")
#positional and Keyword - combo
greet(name="Keerthana",native="INDIA")

print()

#positional, Keyword, Default - combo
def greet(name,age,native="Bangalore"):
    print(f"My name is {name}. I am from {native}")
    print("I am ",age,"years old")
greet("Keerthana",age=26)
greet("Keerthana",age=26,native="INDIA")
