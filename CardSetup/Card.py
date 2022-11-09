class Card(object):
    def __init__(self, val, suit):
        self.suit = suit
        self.value = val

    def show(self):
        print(f"{self.value} of {self.suit}")

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value



