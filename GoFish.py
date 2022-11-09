from CardSetup import Card
from CardSetup.Deck import Deck
from CardSetup.Player import Player
import time
import random


class GoFish(object):
    def __init__(self,player, computer, deck):
        self.deck = deck
        self.player = player
        self.comp = computer


    def initialize(self):
        print(f"Lets begin {self.player.get_name()}!")
        print("drawing 7 cards from the deck...")
        time.sleep(1)
        self.deck.shuffle()
        print("\n")
        for i in range(7):
            self.player.draw(self.deck)
            self.comp.draw(self.deck)

    def computer_move(self):
        print("computer's turn: ")
        time.sleep(1)
        has_it = False
        ranCard = random.choice(self.comp.hand)
        val = ranCard.get_value()
        print(f"Do you have a {val}?")
        print("\n")
        time.sleep(1.5)
        index = []
        for i, c in enumerate(self.player.hand):
            if(c.get_value() == val):
                print("I have the card")
                print("handing over the card...")
                time.sleep(1)
                has_it = True
                index.append(i)
                print(f"computer has obtained: ")
                c.show()
                time.sleep(1)
                print("\n")

        if has_it:
            for j,ind in enumerate(index):
                if ind == index[0]:
                    c = self.player.hand.pop(ind)
                    self.comp.hand.append(c)
                else:
                    c = self.player.hand.pop(ind- j)
                    self.comp.hand.append(c)


        else:
            print(f"You don't have a {val} in your hand")
            time.sleep(0.5)
            print("Go Fish!")
            time.sleep(1)
            self.comp.draw(self.deck)
            print("drawing a card from the deck...")
            time.sleep(1)
            print("computer has drawn a card")
            print("\n")

        time.sleep(1.5)

    def player_move(self):
        print("It is your turn")
        has_it = False
        print("your hand: ")
        time.sleep(1)
        self.player.viewHand()
        print("\n")
        time.sleep(1.5)
        boolean = True
        while boolean:
            val = int(input("Enter the value u want (ex: 1, 2, 3...): "))
            for card in self.player.hand:
                if card.get_value() == val:
                    boolean = False
            if boolean:
                print("Not a valid input... must be a value of a card in your hand. Try again!")
        time.sleep(1)
        print("\n")
        index = []
        for i, card in enumerate(self.comp.hand):
            if (card.get_value() == val):
                print("Opponent has the card")
                print("Handing over the card...")
                time.sleep(1)
                index.append(i)
                has_it = True
                print("You have obtained: ")
                card.show()
                print("\n")
                time.sleep(1)
        if has_it:
            for j,ind in enumerate(index):
                if ind == index[0]:
                    c = self.comp.hand.pop(ind)
                    self.player.hand.append(c)
                else:
                    c = self.comp.hand.pop(ind- j)
                    self.player.hand.append(c)
        else:
            print("Go Fish!")
            time.sleep(1)
            card = self.player.draw(self.deck)
            print("drawing a card from the deck...")
            time.sleep(1)
            print("you have drawn: ")
            card.show()
            time.sleep(1)
            print("\n")
        print(" your hand: ")
        time.sleep(1)
        self.player.viewHand()
        time.sleep(1.5)
        print("\n")

    def checkFourOfKindPlayer(self):
        for card in self.player.hand:
            num_cards = 0
            indeces = []
            for i,c in enumerate(self.player.hand):
                if(c.get_value() == card.get_value()):
                    num_cards +=1
                    indeces.append(i)
            if num_cards == 4:
                print("Got 4 of a kind!")
                print("removing from hand and placing it down...")
                time.sleep(1)
                self.player.points += 1
                for i,index in enumerate(indeces):
                    if index == indeces[0]:
                        self.player.hand.pop(index)
                    else:
                        self.player.hand.pop(index - i)
                print(f"Current Score:\n {self.player.get_name()} has {self.player.points} points \n {self.comp.get_name()} has {self.comp.points}")

                time.sleep(1)

    def checkFourOfAKind(self, user):
        for card in user.hand:
            num_cards = 0
            indeces = []
            for i, c in enumerate(user.hand):
                if(c.get_value() == card.get_value()):
                    num_cards += 1
                    indeces.append(i)
            if num_cards == 4:
                print(f"{user} Got 4 of a kind! ")
                print("removing from hand and placing it down...\n")

                time.sleep(1)
                user.points += 1
                for i, index in enumerate(indeces):
                    if index == indeces[0]:
                        user.hand.pop(index)
                    else:
                        user.hand.pop(index - i)
                print(f"Current Score: \n {self.player.get_name()}: {self.player.points} \n {self.comp.get_name()}: {self.comp.points} \n ")
                time.sleep(1)

    def emptyhand(self, user):
        if not user.hand:
            if not self.deck.cards:
                print("The game is over!")
                time.sleep(1)
                print(f"Score: \n {self.player.get_name()}: {self.player.points} \n {self.comp.get_name()}: {self.comp.points} ")
                quit()
            elif len(self.deck.cards) >= 7:
                for i in range(7):
                    user.draw(self.deck)
            else:
                n = len(self.deck.cards)
                for i in range(n):
                    user.draw(self.deck)


def main():
    print("Lets Play Go Fish!")
    name1 = input("please enter your name player: ")
    comp = Player()
    player = Player(name1)
    deck = Deck()
    game = GoFish(player, comp, deck)
    game.initialize()
    i = 1
    while not (len(player.hand) == 0 & len(comp.hand) == 0 & len(deck.cards) == 0):
        game.emptyhand(player)
        game.player_move()
        game.checkFourOfAKind(player)
        game.emptyhand(comp)
        game.computer_move()
        game.checkFourOfAKind(comp)
        i+=1

    print("The game is over!")
    time.sleep(1)
    print(f"Score: \n {player.get_name()}: {player.points} \n {comp.get_name()}: {comp.points} ")


main()