# Please write a program which keeps asking the user for words. If the user types in end or if the user types in the same word twice in a row loop ends. the program should print out the story the words formed, and finish.

concate = prev = ""
while True:
    word = input("Enter a word: ")
    if word != prev:
        prev = word
    else:
        break
    if word == "end":
        break
    concate+" "+word
print(concate.strip())
