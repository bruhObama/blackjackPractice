from random import randint
import time

suits = ['Hearts','Diamonds','Clubs','Spades']

class Cards:
  def __init__(self, intValue, suit):
    self.intValue = intValue
    self.suit = suit

  def __str__(self):
    return f'{self.intValue} of {self.suit}'
  
def drawCards():
  return Cards(randint(1,10), suits[randint(0,3)])
  
def hitOrStand(x):
  print(f'Your cards sum to {x}.')
  userPrompt = ''

  while userPrompt != 'h' and userPrompt != 's':
    userPrompt = input('Hit or stand?\n[h] [s]\n>>> ')
  return userPrompt

def cardDrawn(y):
  if y != 8:
    print(f'You drew a {y}!')
  else:
    print(f'You drew an {y}!')

def playerHasStood(x,y,z):   # player,house
  print(f'The house flips over their second card. It reads {z}. Overall, their cards sum to {y}')
  time.sleep(0.5)

  if x > y:
    houseIsLosing(x,y,z)
  elif x < y:
    houseHasWon()

def houseIsLosing(x,y,z):   # player,house
  while x > y and y < 17:
    z = drawCards()
    y += z.intValue
    if y > 21:
      print("House bust! you win.")
    else:
      print(f'The house drew {z}! Their cards now sum to {y}.')

def bust(x):
  print(f'Your cards busted at {x}! Game over')
  bustStatus = True
  return bustStatus

def houseHasWon():
  print("The house's cards summed to a higher value than yours! you lose.")

def main():
  houseCardOne = drawCards()
  houseCardTwo = drawCards()
  houseCardTotal = houseCardOne.intValue + houseCardTwo.intValue

  print(f"the House's visible card reads {houseCardOne}. The other will be revealed when you have stood on your deck.")
  time.sleep(0.5)

  playerCard = drawCards()
  playerCardTotal = playerCard.intValue
  cardDrawn(playerCard)
  userPrompt = hitOrStand(playerCardTotal)
  bustStatus = False

  while userPrompt != 's':

    if userPrompt == 'h':
      playerCard = drawCards()
      playerCardTotal += playerCard.intValue

      if playerCardTotal > 21:
        bustStatus = bust(playerCardTotal)
        break

      cardDrawn(playerCard)
      userPrompt = hitOrStand(playerCardTotal)

    else:
     pass

  if bustStatus == True:
    pass
  else:
    playerHasStood(playerCardTotal, houseCardTotal, houseCardTwo)

if __name__ == '__main__':
  main()
