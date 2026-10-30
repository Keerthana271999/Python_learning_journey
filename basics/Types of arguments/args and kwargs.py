#4.arbitrary positional arguments
# * is a must
#accept as a tuple
#since, tuples are immutable
def add(*numbers):
    """Adds given numbers"""
    total=0
    for num in numbers:
        total+=num
    print(f"Sum of {numbers}: {total}")
add(1)
add(1,3,5)
add(1,3,5,7)
add(1,3,5,7,9)

print()

#Combos
def add(list_name,*numbers):
    """Adds given numbers"""
    print(list_name)
    total=0
    for num in numbers:
        total+=num
    print(f"Sum of {numbers}: {total}")
add("Numbers",1,3,5)

print()

def add(*numbers,list_name):
    """Adds given numbers"""
    print(list_name)
    total=0
    for num in numbers:
        total+=num
    print(f"Sum of {numbers}: {total}")
#here, *numbers act as positional so 1st positional then keyword arguments
#act as positional not positional itself. In real they are arbitrary positional
#not normal positional
add(1,3,5,list_name="Numbers")

print()

# ** - arbitrary keyword arguments
# accept as dictionary
def information(**data):
    for key,value in data.items():
        print(key,value)
    print()
information(name="Keerthana")
information(name="Keerthana",age=26)

print()

def information(*numbers,**data):
    total=0
    for num in numbers:
        total+=num
    print(total)
    
    for key,value in data.items():
        print(key,value)
    print()
information(1,2,3,name="Keerthana")
information(1,2,3,4,5,name="Keerthana",age=26)