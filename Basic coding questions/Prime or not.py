# Prime - divisible by 1 and itself
# smallest prime number - 2
# anything b/w 2 to number-1 = not prime

number = int(input("Enter a number: "))
for num in range(2, number):
    if number % num == 0:
        print(f"{number} - not prime")
        break
else:
    print(f"{number} - prime")
