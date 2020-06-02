from player import Player
from deck import Deck

def winner_check(players, deck):
    
    filtered_items = list(filter(lambda p: p.score(deck) < 22, players))

    if len(filtered_items) == 1:
        return f'{filtered_items[0].name} won!'
    elif len(filtered_items) == 0:
        return 'It\'s a tie!'
    
    sorted_players = sorted(filtered_items, key=lambda p: p.score(deck), reverse=True)
    
    if sorted_players[0].score(deck) == sorted_players[1].score(deck):
        return 'It\'s a tie!'
    return f'{sorted_players[0].name} won!'

deck = Deck()
player = Player('Eric', 0)
dealer = Player('Karl', 0)

player.hit(deck.deal())
dealer.hit(deck.deal())

print(player.hand, player.hand[0].to_string())
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
