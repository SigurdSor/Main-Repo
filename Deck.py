""" Dette er et program for å simulere en kortstokk. """
from random import shuffle

suit = [C, D, H, S]
value = list(range(1, 14))
deck = []
for s in suit:
    for v in value:
        deck.append((s,v))
