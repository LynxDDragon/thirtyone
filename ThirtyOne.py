import random


#block that turns the numbers 11-14 into Face Cards
face_cards = {
    11: "J",
    12: "Q",
    13: "K",
    1: "A",
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 1,
}

# make variables for te values and suits
class Cards:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val


    #show the all the cards suits and values
    def show(self):
        print ("{} of {}".format(self.value, self.suit))

#creating an empty list with which to fill the cards when they are created
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        #loop through the list of suits
        for s in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            #while also looping through the values
            for v in range(1,14):
                #pair them and store them into the "self.cards"
                if v in face_cards:
                    card_value = face_cards[v]
                    self.cards.append(Cards(s,card_value))
                else:
                    self.cards.append(Cards(s,v))

    #block that shows the cards
    def show(self):
        for c in self.cards:
            c.show()
    #block that shuffles up the deck
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0, i)
            #rearanges the cards
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.player = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def showHand(self):
        print("Cards in Hand: ")
        for card in self.hand:
            card.show()



class Game:
    def __init__(self):
        self.player = Player("Bryan")

    def start(self):
        print ("The game has started.")
        self.player.draw(deck)
        self.player.draw(deck)
        self.player.showHand()

        while True:
            choice = input("Would you like to draw a card or Stay? (Draw/Stay):  ").lower()


            if choice == "draw":
                self.player.draw(deck)
                self.player.showHand()

            elif choice == "stay":
                print("This is your final hand: ")
                self.player.showHand()
                break
                
deck = Deck()
deck.shuffle()

game = Game()
game.start()


