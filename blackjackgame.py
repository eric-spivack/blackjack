from player import Player
from deck import Deck

def winner_check(players):
    print()

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

filtered_items = filter(lambda p: p.score() < 22, [player, dealer])
winner_check(list(filtered_items))