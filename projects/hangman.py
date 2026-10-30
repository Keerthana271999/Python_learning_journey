import random
fruits = ["apple", "banana"]
chosen = random.choice(fruits)
chosen_fruit = ["_"]*len(chosen)
print(f"fav fruit: {chosen_fruit}")
attempts = 10
while attempts > 0:
    guess = input("guess a letter: ").lower()
    attempts -= 1
    for i in range(len(chosen)):
        if guess == chosen[i]:
            chosen_fruit[i] = guess
    print(f"fav fruit: {chosen_fruit}")
    if attempts == 0 or "_" not in chosen_fruit:
        break
char = ""
for letter in chosen_fruit:
    char += letter
if chosen == char:
    print(f"congrats. you guessed it right")
