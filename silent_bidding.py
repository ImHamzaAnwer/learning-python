from os import system

bidders = {}
bidding = True

def find_highest_bidder():
    highest_bid = 0
    bidder_name = ""
    for name, bid in bidders.items():
        if highest_bid < bid:
            highest_bid = bid
            bidder_name = name
    print(f"winner is {bidder_name} with highest bid of ${highest_bid}")


while bidding:
    name = input("your name? ")
    bid = int(input("your bid ?"))
    bidders[name] = bid

    another_bidder = input("is there another bidder ? type 'yes' or 'no'").lower()

    if another_bidder == "no":
        bidding = False
        find_highest_bidder()
    else:
        system("clear")
