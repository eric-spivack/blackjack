class Player:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []

    def hit(self, card):
        pass
    
    def hand_check(self, deck):
        pass

    def score(self, deck):
        pass

    def to_string(self):
        return f''