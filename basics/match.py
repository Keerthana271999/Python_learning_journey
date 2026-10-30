#MATCH - SIMILAR TO SWITCH IN OTHER LANG, _ - ELSE PART
number=int(input("Number(1-3): "))
match number:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("out of range")
        
number=15
match number%3:
    case 0:
        print("divisible")
    case _:
        print("not divisible")