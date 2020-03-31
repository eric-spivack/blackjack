from card import Card

class Deck:

    def __init__(self):
        self.cards = []
        self.suits = ["clubs", "diamonds", "spades", "hearts"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.new_deck()

    def new_deck(self):
        self.cards = []

        for suit in self.suits:
            for value in self.values:                
                card = Card(suit, value)
                self.cards.append(card)

    def deal(self):
        return self.cards[0]
