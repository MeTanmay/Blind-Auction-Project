import os
from art import logo
print(logo)

value=[]

def winnerrrr():
    highest_bid=0
    winner=""
    for key in bidders:
        current_bid=bidders[key]
        if current_bid>highest_bid:
            highest_bid=current_bid
            winner=key
    print("The winner is " ,winner, " with the bid of ", highest_bid)



bidders={}
more=True
while more:
    a=input("Enter the name of the bidder: ")
    b=int(input("Enter the bid amount: "))
    bidders[a]=b
    que=input("If any more bidders left. Type 'yes' or 'no'.\n")
    if que.lower()=="no":
        winnerrrr()
        break
    else:
        os.system('cls')

#print(bidders)
