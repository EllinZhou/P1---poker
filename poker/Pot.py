from collections import defaultdict

'''
Pot keeps track of each player's bids and community cards
'''


class Pot:

    def __init__(self):
        # pot starts with
        self.money = defaultdict(lambda: 0)
        self.folded_money = 0  # any money belonging to folded players
        self.cards = list()

    def add_bet(self, player, money):
        # TODO: at the player's entry in the money dictionary, add money
        self.money[player] += money

    def add_cards(self, cards):
        # TODO for each card in cards, add the card to self.cards
        # cards = a list of cards from the outside
        # append takes in ONE card and adds it to the list before it
        # extend takes in a LIST of cards and adds every card in that list to the list before it
        # for i in cards:
        #   self.cards.append(i)

        self.cards.extend(cards)

    def balanced(self):
        # TODO: Return true if all the players' money in the pot is the same
        # A 5 B 7 C 5
        # set => (5, 7)
        # A 5 B 5 C 5
        # set => (5)
        # set drops the duplicates
        # numbers = set()
        # for i in self.money.values():
        #     numbers.add(i)
        # # if # of elements is 1 <=> money is same <=> true
        # if len(numbers) == 1:
        #     return True
        # elif len(numbers) > 1:
        #     return False
        money_of_one_player = 0
        for i in self.money.values():
            money_of_one_player = i
            break
        for j in self.money.values():
            if money_of_one_player != j:
              return False
        return True

    def amount_to_call(self, player):
		    # Return amount needed to call for a specific player
        highest_bid = max(value for value in self.money.values())
        return highest_bid - self.money[player]

    def remove_player(self, player):
	      # Remove folded player, adding their money to self.folded_money
        player_money = self.money[player]
        self.folded_money += player_money
        del self.money[player]

    def reward_winner(self, player):
        winnings = sum(self.money.values()) + self.folded_money
        player.add_winnings(winnings)