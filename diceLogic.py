import random 

class Dice:
    def __init__(self, sides, cheatSide, cheatProb=0.33):
        self.sides = sides
        self.cheatSide = cheatSide
        self.cheatProb = cheatProb
    
    def roll(self):
        if random.random() <= self.cheatProb:
            return self.cheatSide
        return random.randint(1, self.sides)

dice = Dice(7, 3)

counts = {}
for i in range(1000):
    value = dice.roll()
    if not counts.get(value):
        counts[value] = 1
    else:
        counts[value] += 1