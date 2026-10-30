import os
bidders_data = {}
while True:
    name = input("what is your name: ")
    bid = int(input("what is your bid: "))
    bidders_data[name] = bid
    more_bidders = input("are there more bidders (yes / no): ").lower()
    if more_bidders == "yes":
        os.system("cls")
    else:
        break
winner = ""
max_bid = 0
for bidder, bid_amount in bidders_data.items():
    if bidders_data[bidder] > max_bid:
        max_bid = bidders_data[bidder]
        winner = bidder
print(f"winner is {winner} with bid amount {max_bid}")
