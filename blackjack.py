################################
#                              #                                     
#       [name redacted]        #
#     Finished 05/03/2020      #
#   Comment Made 09/09/2020    #
#         DD/MM/YYYY           #
#                              #                                            
################################if you see this [name redacted] i'm sorry for slacking

import random
import time
import sys
coin = ["heads","tails"]
housecard1 = 0
housecard2 = 0
yourcardvalue = 0
housecardvalue = 0
choice1 = ""
cardsdrawn = [1,2,3,4,5,6,7,8,9,10,11,11,11]
print("The house starts first.")
time.sleep(1)
housecard1 = random.choice(cardsdrawn)          # generating house's 2 initial cards
housecard2 = random.choice(cardsdrawn)
housecardvalue = housecard1 + housecard2     # summing cards for calculations
print("Face up on the table, you can see the house has",housecard1, "and another card facing down.")       
time.sleep(1)
choice = input("Make your choice\n[h] = Hit\n[s] = Stand")
while choice1 != "s":       # loops until user goes bust or has standed (stood?) using "s"
    if choice == "h":
        time.sleep(1)
        yourcardvalue = random.choice(cardsdrawn) + yourcardvalue    # yourcardvalue is sum of all cards picked up
        print("Your cards sum to ",yourcardvalue)
        if yourcardvalue > 21:
            print("bust")
            break
        choice1 = input("Do you want to stand? \n[s] = stand [h] = hit ")
        if choice1 == "s":
            print("Your cards sum to ",yourcardvalue)
            if yourcardvalue == 21:
              print("BLACKJACK")
            time.sleep(1)
            print("The house had a value of ",housecardvalue)
            if housecardvalue == 21:
              print("BLACKJACK")
            while housecardvalue <= 15 and housecardvalue < yourcardvalue or housecardvalue < yourcardvalue and housecardvalue <= 20:
                housecardvalue = housecardvalue + random.choice(cardsdrawn)
                print("The house hit again!")
                print("The house's cards have a value of ",housecardvalue)
                time.sleep(1)
            if yourcardvalue > 21:
                print("You went bust")
            elif yourcardvalue <= 21 and yourcardvalue > housecardvalue:   # win: less than 21, more than house
                print("You win!")
            elif yourcardvalue <= 21 and yourcardvalue < housecardvalue and housecardvalue <= 21:
                print("The dealer had more than you")
                print("You lost")
            elif yourcardvalue <= 21 and housecardvalue > 21:
                print("dealer bust")
                print("you win")
            elif yourcardvalue <= 21 and housecardvalue <= 21 and yourcardvalue == housecardvalue:
                print("draw, this is awkward. let's flip a coin.")
                coinChosen = input("heads or tails ")
                time.sleep(1)
                coinWinner = random.choice(coin)
                if coinChosen == coinWinner:
                    print("It landed on "+coinWinner+"!")
                    print("you win")
                else:
                    print("It landed on "+coinWinner+". you lose")
