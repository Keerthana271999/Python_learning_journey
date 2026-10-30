#SETS - UNORDERD AND UNIQUE
names={"navin","jenny","sagar","chandan"}
ages={21,32,23,34,324,12,21,456}
print(ages)

#SETS MAY BE HETEROGENOUS
#YOU CANNOT USE COUNT METHOD ON SETS SINCE ALL THE ELEMENTS ARE UNIQUE

#REMOVE - GIVES ERROR IF THE ELEMENT IS NOT THERE
#ages.remove(25)
#print(ages)

#DISCARD - DOES NOT GIVE ERROR
ages.discard(25)
print(names)

#EMPTY SET
empty_set=set()
print(type(empty_set))

print()

#YOU CAN PERFORM MIN MAX SUM

alphabets=set("qwertyuiop")
vowels=set("aeiou")

#SET OPERATIONS
#UNION - COMBINE ALL
print(alphabets|vowels)
#INTERSECTION - CONSIDER COMMON
print(alphabets&vowels)
#DIFFERENCE - EXCEPT COMMON AND OTHER SET ELEMENTS
print(alphabets-vowels)
#SYMMETRIC DIFFERENCE - EXCEPT COMMON
print(alphabets^vowels)
print(vowels.isdisjoint(alphabets))
print(vowels.issubset(alphabets),vowels<=alphabets)
print(vowels.issuperset(alphabets),vowels>=alphabets)
print()

#EXERCISE
a = set("python")
b = set("telusko")
print(a & b)