import random
chosen = random.randint(1, 10)
print("guess a number (1-10)")
difficulty = input("choose difficulty (easy / hard): ")
if difficulty == "easy":
    attempts = 8
else:
    difficulty = 12
while attempts > 0:
    print(f"you have {attempts} attempts")
    attempts -= 1
    guess = int(input("enter a number: "))
    if guess == chosen:
        print(f"congrats. it is {chosen}")
    elif guess < chosen:
        print("number is too less")
    else:
        print("number is too high")
if guess != chosen:
    print(f"number was {chosen}")
