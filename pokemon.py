import numpy as np


class Pokemon:
    def __init__(self):
        self.IV_ATK = np.random.randint(16)
        self.IV_STA = np.random.randint(16)
        self.IN_DEF = np.random.randint(16)

    @property
    def ATK(self):
        return self.BASE_ATK + self.IN_ATK1


    @property
    def ATK(self):
        return self.BASE_STA + self.IN_STA


    @property
    def ATK(self):
        return self.BASE_DEF + self.IN_DEF

    def __str__(self):



class Pikachu(Pokemon):
    BASE_ATL = 112
    BASE_DEF = 101
    BASE_STA = 70


pkmn = Pikachu()
print(pkmi.)
