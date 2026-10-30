#even and odd numbers in a list
numbers=[int(num) for num in input("Enter few numbers: ").split()]
even_count=odd_count=0
for num in numbers:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"Number of even numbers in {numbers} - {even_count}")
print(f"Number of even numbers in {numbers} - {odd_count}")