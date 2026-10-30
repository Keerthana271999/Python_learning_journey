import os

'''file = input("Enter file name: ")
with open(file) as f:
    if os.path.isfile(file) == True:
        print(f"{file}: Available")
    else:
        print(f"{file}: Not available")'''

'''file = input("Enter file name: ")
with open(file) as f:
    if os.path.isfile(file) == True:
        print(f"{file}: Available")
        print()
        with open(file) as f2:
            print(f"The content is: \n{f2.read()}")
    else:
        print(f"{file}: Not available")'''

# NUMBER OF LINES, WORDS, CHARACTERS
'''file = input("Enter file name: ")
lines = words = characters = 0
with open(file, "r") as f:
    if os.path.isfile(file) == True:
        for line in f:
            lines += 1
            words_list = line.split()
            words += len(words_list)
            characters += len(line)
        print(f"{file} has {lines} lines, {words} words, {characters} characters")
    else:
        print(f"{file}: Not Available")'''
