names=["navin","jenny","sagar","chandan"]
ages=[21,32,23,34]

#LISTS MAY BE HETEROGENOUS
navin=["Navin",42,5.6,True]

#YOU CAN PERFORM INDEXING AND SLICING ON LISTS

#LISTS MAY BE NESTED BUT NOT WITH SETS SINCE THEY ARE UNORDERED
name_age=[names,ages]
print(name_age)
print(len(name_age))
print(name_age[0],len(name_age[0]))
print(name_age[0][0])

print()


name_age2=names+ages
print(name_age2)
print(len(name_age2))
print(name_age2[0])

print()

#ADDS SINGLE ELEMENT AT THE END
name_age.append("neso")
print(name_age)

print()

#ADDS MULTIPLE ELEMENTS AT THE END
name_age.extend((1,2,3,4,5))
print(name_age)

print()

#INSERT AT SPECIFIC INDEX, IF INDEX IS NOT THERE INSERT'S AT END
name_age.insert(5,1)
print(name_age)

print()

name_age.insert(100,1)
print(name_age)

print()

#REMOVES FIRST OCCURANCE IN CASE OF DUPLICATES
name_age.remove(1)
print(name_age)

print()

#IF NO INDEX IS SPECIFIED REMOVES LAST ELEMENT AND POPPED ELEMENT CAN BE REUSED
name_age.pop(5)
print(name_age)
popped=name_age.pop()
print(name_age,popped)

#DELETES MULTIPLE ITEMS
del name_age[:2]
print(name_age)

print()

#REVERSE ORIGINAL LIST
name_age.reverse()
print(name_age)
#AT THAT POINT ONLY
name_age[::-1]
print(name_age)

print()

#SORTS ORIGINAL LIST
names.sort()
print(names)
#AT THAT TIME ONLY
print(sorted(names))

#LIST ARE MUTABLE
name_age[4:7]=231,23,32
print(name_age)

print()

print(min(names),max(names))
print(min(ages),max(ages),sum(ages))

print()

#EXERCISE
a = [33, 76, 24, 56]
b = ["navin", "kiran", "harsh"]
print((a[:2] + b[1:])[-3])