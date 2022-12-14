from random import shuffle
from Card import Card
from Suits import Suits
import unittest


class Deck(object):

    card_suits = Suits.SUITS.keys()

    def __init__(self): 
        self.cards = []
        self.create_deck()
        self.shuffle()

    # initialize deck
    def create_deck(self):
        self.cards = [Card(j, i)
                      for i in self.card_suits for j in range(2, 15)]

    # return deck in class format
    def __repr__(self):
        return 'Deck()'

    # return deck in value-suit format
    def __str__(self):
        return str([str(card) for card in self.cards])

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, number_of_cards):
        # TODO deal number_of_cards worth of cards. Should return a list.
        cards = []
        for i in range(number_of_cards):
          c = self.cards.pop()
          cards.append(c)
        return cards


class MyTest(unittest.TestCase):

    def testDeal(self):
        cards = Deck() # use class name to call the constructor
        dealt_cards = cards.deal(4)
        self.assertEqual(len(dealt_cards), 4)
        print(dealt_cards)


if __name__ == '__main__':
    # create a new deck, call deal on it and print the result returned by deal
    unittest.main(argv=['first-arg-is-ignored'], exit=False)