from player import Player
from deck import Deck

deck = Deck()
player = Player('Eric', 0)
dealer = Player('Karl', 0)

player.hit(deck.deal())
dealer.hit(deck.deal())

print(player.hand)
print(dealer.hand)

player.hit(deck.deal())
dealer.hit(deck.deal())

print(player.hand)
print(dealer.hand)
