#! ipython3 -i
from random import randint


class d(object):
    def __init__(self, sides):
        self.sides = sides

    def __add__(self, other):
        if other == d:
            rolls = self(), other()
            return sum(rolls)
        else:
            roll = self()
            return roll + other

    def __radd__(self, other):
        roll = self()
        return roll + other
            

    def __rmul__(self, other):
        rolls = [self.roll() for i in range(other)]
        print(rolls)
        return sum(rolls)

    def __call__(self):
        roll = self.roll()
        print(roll)
        return roll

    def __repr__(self):
        roll = self.roll()
        return str(roll)

    def roll(self):
        roll = randint(1, self.sides)
        return roll


d2, d3, d4, d6, d8, d10, d12, d20 = d(2), d(3), d(4), d(6), d(8), d(10), d(12), d(20)
