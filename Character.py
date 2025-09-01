import random

class Character:
    def __init__(self, name, hp: int, baseDamage: int, parryProb: float, critProb: float):
        self.hp = hp
        self.baseDamage = baseDamage
        self.parryProb = parryProb
        self.critProb = critProb
        self.name = name
        self.ultiUsed = False
        self.ultiTurnsLeft = 0        
    
    def attack(self, enemy):
        damage = self.baseDamage*2 if random.random() <= self.critProb else self.baseDamage
        print(f"Attacking {enemy.name} for {damage} damage.") 
        enemy.recieveDamage(damage)

    def recieveDamage(self, damage: int):
        damageTaken = 0 if random.random() <= self.parryProb else damage
        self.hp -= damageTaken
        print(f"{self.name} received {damageTaken} damage. Current HP: {self.hp}")

    def useUlti(self):
        if self.ultiUsed:
            print(f"{self.name} has already used their ultimate!")
            return False
        self.ultiUsed = True
        return True

    def applyUltiEffect(self):
        if self.ultiTurnsLeft > 0:
            self.ultiTurnsLeft -= 1
            if self.ultiTurnsLeft == 0:
                self.endUltiEffect()

    def endUltiEffect(self):
        pass


class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20, 0.10, 0.45)

    def useUlti(self):
        if super().useUlti():
            print(f"{self.name} activates Script Power! Double crit chance for 3 turns!")
            self.critProb *= 2
            self.ulti_turns_left = 3

    def endUltiEffect(self):
        self.critProb /= 2
        print(f"{self.name}'s Script Power has ended.")

class Tank(Character):
    def __init__(self, name):
        super().__init__(name, 500, 15, 0.55, 0.25)
    
    def useUlti(self):
        if super().useUlti():
            print(f"{self.name} activates Iron Wall! Double parry chance for 2 turns!")
            self.parryProb *= 2
            self.ulti_turns_left = 2

    def endUlti(self):
        self.parryProb /= 2
        print(f"{self.name}'s Iron Wall has ended.")


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10, 0.1, 0.6)

    def useUlti(self):
        if super().useUlti():
            print(f"{self.name} casts Arcane Surge! Double damage for 2 turns!")
            self.baseDamage *= 2
            self.ulti_turns_left = 2

    def endUltiEffect(self):
        self.baseDamage //= 2
        print(f"{self.name}'s Arcane Surge has ended.")

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, 350, 10, 0.55, 0.1)

    def useUlti(self):
        if super().useUlti():
            print(f"{self.name} uses Divine Blessing: Heal 50 HP per turn for 3 turns!")
            self.ultiTurnsLeft = 3

    def applyUltiEffect(self):
        if self.ultiTurnsLeft > 0:
            self.hp += 50
            print(f"{self.name} is healed by Divine Blessing! Current HP: {self.hp}")
            self.ultiTurnsLeft -= 1
            if self.ultiTurnsLeft == 0:
                self.endUltimateEffect()

    def endUltiEffect(self):
        print(f"{self.name}'s Divine Blessing has ended.")
