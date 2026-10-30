#OPERATOR OVERLOADING
# + with numbers - adds
# + with text - concatenate
# * with numbers - multiplies
# * with text - repeats
print("navin "+"telusko")

print()

#INDEXING - fetches single value at a time
#gives index out of range error if index is not there
#LHS - RHS = index start from 0
#RHS - LHS = index start from -1
#position / location = strat from 1

#SLICING - fetches single value at a time
#does not give error if index is not there, instead goes till the end
#LHS - RHS = index start from 0
#RHS - LHS = index start from -1
#position / location = strat from 1
#SYNTAX - [strat:stop:step]
#by default start=0, stop=always give +1 value, step=1

text="telusko"
print(len(text))

print()

print(text[0],text[1],text[3],text[6],text[-1],text[-7])
print(text[3:],text[:3])

#STRINGS ARE IMMUTABLE
#text[:3]="TEL"
print(text[:3].upper()+text[3:])

print()

navin="My name is Navin Reddy\nWelcome to telusko"
print(navin)

print()

#EXERCISE
text="Telusko"
print(text[-6:6])