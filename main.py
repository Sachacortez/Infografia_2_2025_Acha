from Character import Character
from Character import Rogue, Tank, Wizard, Paladin
import random

players = input("Enter the amount of players (2-4): ")
characters = input("Enter the characters (Rogue, Tank, Wizard, Paladin)").split(",")
names = input("Enter the names of the characters (comma separated): ").split(",")
turns = int(input("Enter the number of turns: "))

for i, char in enumerate(characters):
    if char.strip().lower() == "rogue":
        characters[i] = Rogue(names[i].strip())
    elif char.strip().lower() == "tank":
        characters[i] = Tank(names[i].strip())
    elif char.strip().lower() == "wizard":
        characters[i] = Wizard(names[i].strip())
    elif char.strip().lower() == "paladin":
        characters[i] = Paladin(names[i].strip())

for turn in range(turns):
    for c in characters:
        c.applyUltiEffect()
    random.shuffle(characters)
    currentPlayer = characters[0]
    print(f"Now it's {currentPlayer.name}'s turn.")
    
    action = input("Choose action: (A)ttack or (U)ltimate: ").strip().lower()

    if action == "u":
        currentPlayer.useUlti()
        continue


    enemy = input("Choose an enemy to attack: ").strip().lower()
    if enemy not in [char.name.lower() for char in characters]:
        print("Invalid enemy choice. Try again.")
    elif enemy == currentPlayer.name.lower():
        print("You cannot attack yourself. Choose another enemy.")
    else:
        for char in characters:
            if char.name.lower() == enemy.strip().lower():
                characters[0].attack(char)
                if char.hp < 0:
                    char.attack(characters[0])
                break
            

for char in characters:
    if char.hp > 0:
        print(f"{char.name} survived with {char.hp} HP left.")
    else:
        print(f"{char.name} has been defeated.")

print("Game Over.")