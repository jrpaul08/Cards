import time
class Player(object):
    def __init__(self, name="Computer"):
        self.name = name
        self.hand = []
        self.points = 0

    def get_name(self):
        return self.name

    def draw(self,deck):
        card = deck.drawCard()
        self.hand.append(card)
        return card


    '''
    def viewHand(self):
        for card in self.hand:
            card.show()
            time.sleep(0.5)
    
'''
    def viewHand(self):
        for i in range(14):
            for card in self.hand:
                if card.get_value() == i:
                    card.show()
                    time.sleep(0.4)