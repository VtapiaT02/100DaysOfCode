print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

print("You stand at a crossroads, two paths stretching out before you.")
print("Your adventure begins now. Choose wisely, for your destiny depends on it.")
road = input("Which path will you take? Left or Right?\n").lower()

if road == "left" or road == "l":
    print("\nBrave choice! You step onto the left path, the forest whispering secrets around you.")
    print("Suddenly, you face your first challenge.\n")

    print("Before you lies a raging river, its currents swift and unforgiving.")
    print("You can either attempt to swim across or wait patiently for something to happen.")
    action = input("What will you do? Swim or Wait?\n").lower()

    if action == "wait" or action == "w":
        print("\nWise patience. Time seems to slow as you watch the river.")
        print("Suddenly, a sturdy bridge materializes, inviting you to cross safely.")
        print("You have passed this challenge!\n")

        print("Ahead stands a grand doorframe with three doors: one red, one blue, and one yellow.")
        print("Only one will lead you to victory, the others to peril.")
        print("Choose carefully — your final test awaits!")
        door = input("Which door will you open? Blue, Red, or Yellow?\n").lower()

        if door == "red" or door == "r":
            print("\nAs you open the red door, flames burst forth, engulfing you in searing heat.")
            print("You have been burned by fire.\nGame Over.")
        elif door == "blue" or door == "b":
            print("\nThe blue door creaks open to reveal snarling beasts that leap at you.")
            print("You have been eaten by beasts.\nGame Over.")
        elif door == "yellow" or door == "y":
            print("\nLight floods the room as you step through the yellow door.")
            print("Congratulations, you have found the treasure and won the game!")
            print("YOU WIN!")
        else:
            print("That path was never meant to be taken. Fate does not forgive the unwise.\nGame Over.")

    elif action == "swim" or action == "s":
        print("\nYou dive into the river, but the currents are too strong.")
        print("A swarm of fierce trout attack you as you struggle to stay afloat.")
        print("You have been attacked by a trout.\nGame Over.")
    else:
        print("That path was never meant to be taken. Fate does not forgive the unwise.\nGame Over.")

elif road == "right" or road == "r":
    print("\nYou take the right path, but the ground suddenly gives way beneath your feet.")
    print("You fall into a deep, dark hole.")
    print("Game Over.")
else:
    print("That path was never meant to be taken. Fate does not forgive the unwise.\nGame Over.")
