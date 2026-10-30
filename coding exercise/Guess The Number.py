import random
print("guess a number (1-50)")
number = random.randint(1, 50)
difficulty = input("Choose difficulty level (easy / hard): ").lower()
if difficulty == "easy":
    attempts = 10
else:
    attempts = 15
print(f"You have {attempts} attempts")
while attempts > 0:
    guess = int(input("Guess a number: "))
    attempts -= 1
    if guess == number:
        print(f"Congrats: It is {guess}")
    elif guess < number:
        print(f"Number is too low")
        print(f"You have {attempts} attempts left")
    else:
        print(f"Number is too high")
        print(f"You have {attempts} attempts left")
    if attempts == 0 and guess != number:
        print("Out of lives")
        print(f"The number was {number}")
        break
