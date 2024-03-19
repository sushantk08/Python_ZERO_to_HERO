import os
bidder_data={}
flag=False

def bidder_details(bidder_data):
    highest_bid=0
    winner=""
    for bidder in bidder_data:
        bid=bidder_data[bidder]
        if bid>highest_bid:
            highest_bid=bid
            winner=bidder
    print(f'winner is {winner} with {highest_bid} bid')
while not flag:
    name=input("enter bidder name: ")
    ammount=int(input("enter bid ammount: "))
    bidder_data[name]=ammount


    more_bidders=input("are there more bidder? type 'yes' or 'no': ").lower()

    if more_bidders=="yes":
        os.system('cls')
        flag=False
    elif more_bidders=="no":
        flag=True
        os.system('cls')
        bidder_details(bidder_data)
