#Recurssion - function calling itself and function is called recursive function
#Anything pending will be performed at the time of returning
#We must have a terminating condiong to stop or else it will be infinite recursive function

#TYPES
#1. Tail
def function(number):
    if number>0:
        print(number,end=" ")
        function(number-1)
x=3
function(x)

print()

#2. Head
def function2(number):
    if number>0:
        function2(number-1)
        print(number,end=" ")
x=3
function2(x)

print()

#3. Indirect( one calling other in circular fashion)
#A-->B-->C-->A
def function3(number):
    if number>0: 
        print(number,end=" ") 
        function4(number-1) 
def function4(number):
    if number>1: 
        print(number,end=" ") 
        function3(number//2) 
function3(20)

print()

#4. Nested( one inside other as parameter)
def function5(number):
    if number>100:
        return number-10
    else:
        return function5(function5(number+11))
print(function5(95))