import random
alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
             "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols_list = ["@", "#", "$", "%", "&", "_"]
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = int(input("Number of letters: "))
numbers = int(input("Number of numbers: "))
symbols = int(input("Number of symbils: "))
easy = ""
for l in range(letters):
    l_chosen = random.choice(alphabets)
    easy += l_chosen
for s in range(symbols):
    s_chosen = random.choice(symbols_list)
    easy += s_chosen
for n in range(numbers):
    n_chosen = random.choice(numbers_list)
    easy += str(n_chosen)
easy = list(easy)
hard = ""
random.shuffle(easy)
for char in easy:
    hard += char
print(f"password: {hard}")
