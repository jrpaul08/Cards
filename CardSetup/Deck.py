import random
from CardSetup.Card import Card
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["spades", "clubs", "diamonds", "hearts"]:
            for val in range(1, 14):
               self.cards.append(Card(val, suit))


    def showDeck(self):
        for card in self.cards:
            card.show()

    def showValues(self):
        for card in self.cards:
            card.get_value()

    def showSuits(self):
        for card in self.cards:
            card.get_suit()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            rand = random.randint(0,i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]


    def drawCard(self):
        return self.cards.pop()
