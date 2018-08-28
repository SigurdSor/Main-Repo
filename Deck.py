""" Dette er et program for å simulere en kortstokk. """
from random import shuffle
class Deck():
    def __init__(self):
        suit = ["C", "D", "H", "S"]
        value = list(range(1, 14))
        self.deck = []
        for s in suit:
            for v in value:
                self.deck.append((s,v))

    def __str__(self):
        return (str(self.deck))

    def shuffle(self):
        shuffle(self.deck)

    def draw(self, n=1):
        return [self.deck.pop() for _ in range(n)]

    def sort(self):
        self.deck.sort()

"""
kortstokk = Deck()
kortstokk.shuffle()
print(kortstokk.draw(5))
print(kortstokk)
kortstokk.sort()
print(kortstokk)
"""
