class Player:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []

    def hit(self, card):
        self.hand.append(card)

    def hand_check(self, deck):
        score = self.score(deck)
        fulcrum = 15

        if score >= fulcrum:
            return False

        return True

    def score(self, deck):
        return deck.score(self.hand)