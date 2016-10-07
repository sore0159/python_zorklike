# Strings ["S", "C", "D", "H"] for suits, for now
# Might want a better way to do that, but it works.
class Card:
    def __init__(self, val, suit):
        self.value = val
        self.suit = suit
    def __repr__(self):
        return "%d of %s"%(self.value, self.suit)

# Most of these are kinda standard list operations
# Could be abstracted out, but eh...
#
# Also I might convert some list constructions here to use
# list comprehensions, which are pretty cool but I don't remember
# exactly how to use
#
# The "top" of the deck is the last card in the self.cards list
class Deck:
    def __init__(self):
        cards = [];
        for i in range(13):
            for suit in ["S", "C", "D", "H"]:
                card = Card(i+1, suit)
                cards.append(card)
        self.cards = cards
    def __repr__(self):
        return "Deck of %d Cards"%len(self.cards)
    def shuffle(self):
        pass  #todo
    def draw(self, n):
        cards = [];
        for i in range(n):
            if len(self.cards) == 0:
                break
            cards.append(self.cards.pop())
        return cards
    def return_top(self, card):
        self.cards.append(card)
    def peek(self, n):
        cards = []
        for i in range(len(self.cards)):
            if i >= n:
                break
            cards.append(self.cards[len(self.cards)-(i+1)])
        return cards


# neat trick for testing:
# this part only runs if the file is called directly via
#
# python card.py
if __name__ == "__main__":
    test = Card(1, "D")
    print("TEST CARD:", test)
    test = Deck()
    print("TEST DECK:", test)
    draw = test.draw(10)
    print("TEST DRAW:", draw)
    test.return_top(draw[0])
    print("TEST PEEK:", test.peek(5))
    print("TEST PEEK:", test.peek(5))
