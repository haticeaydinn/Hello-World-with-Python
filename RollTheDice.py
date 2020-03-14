import random


class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        # my_tuple = (x, y)
        # return my_tuple
        return x, y


dice = Dice()
print(dice.roll())
