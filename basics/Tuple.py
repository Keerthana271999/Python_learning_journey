names=("navin","jenny","sagar","chandan")
ages=(21,32,23,34)

#TUPLES MAY BE HETEROGENOUS
#YOU CAN PERFORM INDEXING AND SLICING ON TUPLES
#TUPLES MAY BE NESTED BUT NOT WITH SETS SINCE THEY ARE UNORDERED

#TUPLES ARE IMMUTABLE, HENCE CAN COVERT TO LIST AND MAKE IT MUTABLE
names_list=list(names)
names_list.append("neso")
names=tuple(names_list)
print(names)

print()

name_age=("navin","harsh",[21,213,1])
name_age[2][1]=23
print(name_age)

#SINGLE ELEMENT TUPLE
single_element=(1,)
print(type(single_element))

print()

#YOU CAN PERFORM MIN MAX SUM

print()

#EXERCISE
tup = (50, 70, 90)
x = tup[0]
y = tup[2]
print(x + y)