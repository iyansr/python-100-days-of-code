from art import logo

print(logo)

bids = {}
is_finished = False


def go_bid():
    name = input("What is your name ? ")
    bid_price = int(input("How much you want to bid $"))
    bids[name] = bid_price


def get_highest_bid():
    highest = 0
    person = ""
    for key in bids:
        if bids[key] > highest:
            highest = bids[key]

        if highest == bids[key]:
            person = key

    print(f"The winner is {person} with the highest bid of ${highest}")


while not is_finished:
    go_bid()
    has_other_bidder = input("Are there any other bidders ? type 'yes' or 'no' : ")
    if has_other_bidder == "yes":
        is_finished = False
    elif has_other_bidder == "no":
        is_finished = True

get_highest_bid()
