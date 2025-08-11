import random

sidesAmount = int(input("How many sides does your dice have? "))
turnsAmount = int(input("How many turns will there be? "))

for turn in range(turnsAmount):
    dice_value = random.randint(1, sidesAmount)
    print(f"The dice shows: {dice_value}")
    input ("Press Enter to roll the dice again...")

print("END OF THE GAME")