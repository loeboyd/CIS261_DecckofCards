#Lois Daniels
#CIS261
#06June24

import random

class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

class Deck:
	def __init__(self):
		self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9','10', 'Jack', 'Queen', 'King']
		self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
		self.reset()
		
	def reset(self):
		self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
		
	def shuffle(self):
		random.shuffle(self.deck)
		
	def deal(self):
		if len(self.deck) == 0:
			return None
		return self.deck.pop()
		
	def count(self):
		return len(self.deck)
		
print("Welcome to the Card Dealer!")
print("There is a deck of 52 cards.")

# Create a deck
deck = Deck()

# Shuffle the deck
deck.shuffle()

# Ask user for the number of cards to deal
num_cards_to_deal = int(input("How many cards would you like to deal?  "))
dealt_cards = []

# Deal the requested number of cards
for _ in range(num_cards_to_deal):
	card = deck.deal()
	if card is not None:
		dealt_cards.append(f"{card.rank} of {card.suit}")
	else:
		print("No more cards in the deck.")
		break
		
# Display the dealt cards
if dealt_cards:
	print("Dealt cards:")
	for card in dealt_cards:
		print(card)
		
# Display remaining card count
remaining_count = deck.count()
print(f"Remaining cards in the deck: {remaining_count}")

print("Good Luck!")
