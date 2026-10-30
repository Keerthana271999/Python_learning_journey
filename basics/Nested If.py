number=int(input("Number (1-10): "))
if number>0:
    print("+ve")
    if number%2==0:
        print("even")
    else:
        print("odd")
else:
    print("-ve")
    

marks = 72

if marks >= 50:
    print("Pass")
    if marks >= 75:
        print("Distinction")
    else:
        print("Average")
else:
    print("Fail")

print("End of Evaluation")