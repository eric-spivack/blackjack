import pytest
from src.blackjackgame import winner_check
from src.deck import Deck


def test_deck_suit_length():
    d = Deck()
    assert len(d.suits) == 4

def test_deck_values():
    assert True
