from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    # {"Radek": 7, "Jana": 8}
    highest_bid = 0
    winner = ""
    for name in bidding_record:
        bid_ammount = bidding_record[name]
        if bid_ammount > highest_bid:
            highest_bid = bid_ammount
            winner = name
    print(f"Vítězem je {winner} s nabídkou {highest_bid} Kč!")       
while not bidding_finished:
    name = input("Zadejte jméno: ")
    bid = int(input("Zadejte částku: "))
    bids[name] = bid
    next_bid = input("Chcete zadat další jméno? A/N ")
    if next_bid == "N":
        bidding_finished = True
        find_highest_bidder(bids)
    elif next_bid == "Y":
        clear()
        print(logo)
