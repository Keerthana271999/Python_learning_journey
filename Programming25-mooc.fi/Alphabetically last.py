# Python comparison operators can also be used on strings. Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last. You can assume all words will be typed in lowercase entirely.

word1 = input("Enter 1st word: ").strip().lower()
word2 = input("Enter 2nd word: ").strip().lower()
if word1 < word2:
    print(word2, "comes alphabetically last")
elif word1 > word2:
    print(word1, "comes alphabetically last")
else:
    print("You gave same word")
