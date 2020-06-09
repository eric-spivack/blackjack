from player import Player
from deck import Deck

def winner_check(players, deck):
    pass

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

if player.hand_check(deck):
    dealt_card = deck.deal() 
    player.hit(dealt_card)
      
if dealer.hand_check(deck):
    dealt_card = deck.deal()
    dealer.hit(dealt_card)

print(winner_check([player, dealer], deck))
