import time
import random
cards_in_deck = [1,2,3,4,5,6,7,8,9,10,11,11,11]
power_cards = ["king","queen","jack"]
cards_for_later = []

def house_initial_card_draw(x):
  first_card_drawn_house = random.choice(cards_in_deck)
  second_card_drawn_house = random.choice(cards_in_deck)
  if x:
    return first_card_drawn_house    # gives visible card on desk because 1 == True
  else:
    return first_card_drawn_house + second_card_drawn_house  # gives sum of cards because 0 == False
  
def player_card_draw():
  card_drawn_player = random.choice(cards_in_deck)
  return card_drawn_player

def power_card_drawn(x):
  power_card_drawn = random.choice(power_cards)
  if x:
    print("The house drew a "+power_card_drawn+"!") # 1 - House
  else:
    print("You drew a "+power_card_drawn+"!") # 0 - Player
    return 11

def house_hit():
  house_hit = random.choice(cards_in_deck)
  while house_hit == 11:
    house_hit = random.choice(cards_in_deck)
  return house_hit

def gameplay():
  house_total_cards_hidden = house_initial_card_draw(0) # house_total_cards_initial is a dumb variable name sorry
  houses_visible_cards = house_initial_card_draw(1)
  player_card_drawn = player_card_draw()   # it's player_cards_total for the sum,it's player_card_drawn for the individual card xoxoxox
  player_cards_total = player_card_drawn
  time.sleep(1)
  if houses_visible_cards != 11 and houses_visible_cards != 8:
    print("The house draws a",houses_visible_cards,"and another, hidden card.")
    time.sleep(0.5)
  elif houses_visible_cards == 8:
    print("The house draws an",houses_visible_cards,"and another, hidden card.")
    time.sleep(0.5)
  else:
    power_card_drawn(1)
    time.sleep(0.5)
    print("Their (visible) cards sum to ",houses_visible_cards,".")
    time.sleep(0.5)
  if player_card_drawn != 11:
    print("The house gives you your card. You drew",player_card_drawn,". Your cards sum to",player_cards_total,".")
    time.sleep(0.5)
  else:
    time.sleep(0.5)
    player_cards_total + power_card_drawn(0)
    time.sleep(0.5)
    print("Your cards sum to ",player_cards_total,".") 
  print("[h] Hit\n[s] Stand\n")
  hit_or_stand = ""   
  while hit_or_stand != "s":
    hit_or_stand = input(">>> ")  
    if hit_or_stand == "h":
      player_card_drawn = player_card_draw()
      if player_card_drawn != 11 and player_card_drawn != 8:
        print("You drew a",player_card_drawn,"!")
        player_cards_total += player_card_drawn
        time.sleep(1)
        print("Your cards sum to",player_cards_total,"!")
      elif player_card_drawn == 8:
        print("You drew an",player_card_drawn,"!")
        player_cards_total += player_card_drawn
        time.sleep(1)
        print("Your cards sum to",player_cards_total,"!")
      else:
        player_cards_total += power_card_drawn(0)
        print("Your cards sum to",player_cards_total,"!")
    if player_cards_total > 21:
      hit_or_stand = "s"
  player_stood = True
  while player_stood == True:
    print("The house's cards sum to ",house_total_cards_hidden)
    while house_total_cards_hidden <= 15 and house_total_cards_hidden < player_cards_total or house_total_cards_hidden < player_cards_total and house_total_cards_hidden <= 20 and player_cards_total < 22:
       house_total_cards_hidden += house_hit()
       print("The house hit again!")
       time.sleep(0.5)
       print("The house's cards sum to ",house_total_cards_hidden)
    player_stood = False
    cards_for_later.append(player_cards_total)
    cards_for_later.append(house_total_cards_hidden)
    endgame()

def endgame():      # decides what ending player is going to recieve
  player_cards_total = cards_for_later[0]
  house_total_cards_hidden = cards_for_later[1]
  if player_cards_total < 21 and player_cards_total > house_total_cards_hidden:
    blackjack_game_won()
  elif house_total_cards_hidden > 21 and player_cards_total < 22:
    blackjack_game_dealer_bust()
  elif player_cards_total > 21:
    player_bust()
  elif house_total_cards_hidden == player_cards_total:
    blackjack_game_has_drawn()
  elif house_total_cards_hidden > player_cards_total:
    blackjack_game_lost()
  
def blackjack_game_won():
  print("You win!")

def blackjack_game_lost():
  print("The dealer has a higher card value than you, you lose.")

def player_bust():
  print("Your cards went over 21! You lose")

def blackjack_game_dealer_bust():
  print("The dealers cards have gone over 21! You win.")

def blackjack_game_has_drawn(): # function for player cards == dealer cards
  coins = ["heads","tails"] # array contains 2 sides of coins
  coin_chosen = "" # so this shitty while loop works
  print("draw, this is awkward. let's flip a coin.")
  while coin_chosen != "heads" and coin_chosen != "tails": # while the coin chosen is not a head or tail input will repeat
    coin_chosen = input("heads or tails ") #coin_chosen = chosen head or tail
  time.sleep(1)
  coinWinner = random.choice(coins)
  if coin_chosen == coinWinner:
    print("It landed on "+coinWinner+"!")
    print("you win")
  else:
    print("It landed on "+coinWinner+". you lose")

if __name__ == "__main__":
 gameplay()
