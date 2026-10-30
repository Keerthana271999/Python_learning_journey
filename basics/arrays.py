#ARRAY - HOMOGENOUS DATA
#NO UNICODE CHARACTER FOR STRINGS, USE LISTS / TUPLE.....
import array
numbers=array.array("i",[21,12,3123,23])
for num in numbers:
    print(num,end=" ")
print(type(numbers))

numbers2=array.array("f",[2.5,4.8,-3.2,6.7])
for num in numbers2:
    if num<0:
        continue
    print(num,end=" ")
    
print()

#INDEX STARTS AT 0
start=0
while start<=len(numbers2)-1:
    if numbers2[start]<0:
        start+=1
        continue
    print(numbers2[start],end=" ")
    
#TRY LIST METHODS APPEND ... FOR ARRAYS
    start+=1