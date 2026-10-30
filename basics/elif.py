number=int(input("Number (1-5): "))
if number==1:
    print("one")
elif number==2:
    print("two")
elif number==3:
    print("three")
elif number==4:
    print("four")
elif number==5:
    print("five")
else:
    print("out of range")
    
score=54
if score>=90:
    print("A+")
elif score>=75 and score<=89:
    print("A")
elif score>=60 and score<=74:
    print("B+")
else:
    print("B")