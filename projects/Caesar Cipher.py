alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def encryption():
    msg = input("Enter uour msg: ")
    shift = int(input("Enter shift key: "))
    ciphaer = ""
    for letter in msg:
        pos1 = alphabets.index(letter)
        pos2 = (pos1+shift) % 26
        ciphaer += alphabets[pos2]
    print(f"ciphaer text: {ciphaer}")


def decryption():
    msg = input("Enter uour msg: ")
    shift = int(input("Enter shift key: "))
    plain = ""
    for letter in msg:
        pos1 = alphabets.index(letter)
        pos2 = (pos1-shift) % 26
        plain += alphabets[pos2]
    print(f"plain text: {plain}")


while True:
    choice = input("choose one encrypt / decrypt / none: ").lower()
    if choice == "encrypt":
        encryption()
    elif choice == "decrypt":
        decryption()
    else:
        break
