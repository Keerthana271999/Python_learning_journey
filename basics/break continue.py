'''for number in range(1,11):
    if number%3==0:
        continue
    print(number,end=" ")'''
    
'''for number in range(1,11):
    if number==6:
        break
    print(number,end=" ")'''
    
print()

'''start=1
while start<=10:
    if start%3==0:
        start+=1
        continue
    print(start,end=" ")
    start+=1'''
    
'''start=1
while start<=10:
    if start==6:
        break
    print(start,end=" ")
    start+=1'''
    
for num in range(10):
    if num % 3 == 0:
        continue
    if num == 8:
        break
    print(num,end=" ")