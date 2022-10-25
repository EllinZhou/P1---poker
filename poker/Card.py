from Suits import Suits
from FaceValues import FaceValues
import unittest


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.suit_symbol = Suits.SUITS[self.suit]

    def __eq__(self, other):
         
        # TODO is self equal to other? Return True if self and other are both cards, else False
        return self.value == other.value and self.suit == other.suit

    def __gt__(self, other):
        # TODO is self greater than other? if self > other, return True
        return self.value > other.value

    # representation of object for developer (i.e., Card(value=4, suit='Hearts'))
    def __repr__(self):
        return 'Card(value=%r, suit=%r)' % (self.value, self.suit)

    # representation of object for player
    def __str__(self):
        return str(FaceValues.FACEVALUES[self.value]) + str(self.suit_symbol)

    def color(self):
        # TODO return 'red' or 'black' depending on suit of card
        # red: hearts, diamonds
        # black: clubs, spades
        if self.suit == "Hearts" or self.suit == "Diamonds":
            return 'red'
        else:
            return 'black'


class MyTest(unittest.TestCase):
    def testCard(self):
        c = Card(10, Suits.HEARTS)
        self.assertTrue(c.value == 10)
        self.assertTrue(c.suit == Suits.HEARTS)

    def test__eq__(self):
        # TODO: Write a test
        c1 = Card(10, Suits.HEARTS)
        c2 = Card(10, Suits.HEARTS)
        self.assertTrue(c1 == c2)
        c3 = Card(9, Suits.DIAMONDS)
        self.assertFalse(c1 == c3)
    
    def test__gt__(self):
        # TODO: Write a test
        c1 = Card(10, Suits.HEARTS)
        c2 = Card(10, Suits.HEARTS)
        self.assertFalse(c1 > c2)
        c3 = Card(9, Suits.DIAMONDS)
        self.assertTrue(c1 > c3)

    def test__repr__(self):
        c = Card(10, Suits.HEARTS)
        self.assertEqual(c.__repr__(), 'Card(value=10, suit=\'Hearts\')')

    def test__str__(self):
        # TODO: Write a test
        c = Card(10, Suits.HEARTS)
        self.assertEqual(c.__str__(), "10♥")
        c1 = Card(11, Suits.SPADES)
        self.assertEqual(c1.__str__(), "J♠")
        


if __name__ == '__main__':
    # c = Card(10, Suits.HEARTS)
    # print(c)
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
 