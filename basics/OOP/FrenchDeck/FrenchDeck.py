"""
Magic methods
"""
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JOKA')
    """
    ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'O', 'K', 'A']
    """
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print("\n***All cards***")
    for card in deck:
        print(card)