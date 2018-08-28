""" Dette er en enkel funksjon for å plukke ut alle tallene som er mindre enn en gitt verdi"""

def less_than(original, n):
    return [i for i in original if i<n]

"""Test"""
def less_than_test():
    a = [1, 2, 3, 4, 5]
    b = 3

    c = less_than(a, b)

    known_awnser = [1, 2]
    assert known_awnser == c

less_than_test()
