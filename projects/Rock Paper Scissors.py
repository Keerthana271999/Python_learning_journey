from rock_paper_scissor_exception import RockPaperScissor
import random
choices = ["rock", "paper", "scissor"]
your_choice = input("rock / paper / scissor: ").lower()
computer_choice = random.choice(choices)
try:
    if your_choice not in choices:
        pass
        raise RockPaperScissor("this game has only 3 choices")
except RockPaperScissor as msg:
    print(f"Error: {msg.__class__.__name__}")
    print(f"Message: {msg}")
    exit()
if your_choice == computer_choice:
    print(f"you - {your_choice}, computer - {computer_choice}: Tie")
elif your_choice == "rock":
    if computer_choice == "paper":
        print(
            f"you - {your_choice}, computer - {computer_choice}: computer win's")
    else:
        print(f"you - {your_choice}, computer - {computer_choice}: you won")
elif your_choice == "paper":
    if computer_choice == "rock":
        print(f"you - {your_choice}, computer - {computer_choice}: you won")
    else:
        print(
            f"you - {your_choice}, computer - {computer_choice}: computer win's")
else:
    if computer_choice == "rock":
        print(
            f"you - {your_choice}, computer - {computer_choice}: you won")
    else:
        print(
            f"you - {your_choice}, computer - {computer_choice}: computer win's")
