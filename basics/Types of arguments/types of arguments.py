def greet(name,dept,clg="PES"):
    print(f"Hi my name is {name}. I am from {dept} department")
    print(f"I sudied in {clg}")
greet("Keerthana",dept="EC")

print()

greet("Keerthana","EC","Surana")
greet("Keerthna",dept="EC",clg="Surana")

print()

def addition(list_name,*numbers):
    print(list_name,"\n")
    total=0
    for num in numbers:
        total+=num
    print("Sum",total)
addition("Numbers",1)
addition("Numbers",1,3,5)
addition("Numbers",1,3,5,7,9)

print()

def information(*numbers,**data):
    res=1
    for num in numbers:
        res*=num
    print("information",res)
    
    print()
    
    for key,value in data.items():
        print(f"{key}:{value}")
        
    print()
    print()
    
information(2,3,-6,8,name="Keerthana")
information(2,5,8,9,0,6,name="Keeerthana",age=26)
information(1,2,3,4,5,name="Keeerthana",age=26,height=5.5)