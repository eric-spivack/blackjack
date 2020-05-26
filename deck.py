from card import Card
import random

class Deck:

    def __init__(self):
        self.cards = []
        self.suits = ["clubs", "diamonds", "spades", "hearts"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.values_map = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 1
        }
        self.new_deck()

    def new_deck(self):
        self.cards = []

        for suit in self.suits:
            for value in self.values:                
                card = Card(suit, value)
                self.cards.append(card)

    def deal(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

    def score(self, cards):
        total = 0

        for card in cards:
            total += self.values_map[card.value]
        return total