class Deck:

    def __init__(self):
        self.cards = []

    def new_deck(self):
        self.cards = []
        suits = ["clubs", "diamonds", "spades", "hearts"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]