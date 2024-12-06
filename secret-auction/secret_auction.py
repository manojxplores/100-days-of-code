import os

print("Welcome to the secret auction program.")
bids = {}
continue_auction = True

def find_highest_bidder(auction_dict):
    highest_bid = 0
    highest_bidder = ""
    for bidder in auction_dict:
        if auction_dict[bidder] > highest_bid:
            highest_bid = auction_dict[bidder]
            highest_bidder = bidder
    return highest_bidder, highest_bid

while continue_auction:
    user_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    bids[user_name] = bid_amount

    if input("Are there any other bidders? Type 'yes' or 'no'.") == "no":
        continue_auction = False
        os.system("cls")
    else:
        os.system("cls")

highest_bidder, highest_bid = find_highest_bidder(bids)
print(f"The winner is {highest_bidder} with a bid of ${bids[highest_bidder]}.")