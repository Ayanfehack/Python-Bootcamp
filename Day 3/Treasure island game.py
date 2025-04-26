print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to treasure island\nYour mission is to find the missing Treasure buried deep in the island.")
way = input('You are at a crossroad, where do you want to go? Type "left" or "right". \n').lower()

if way == "left":
    cross = input('You\'ve arrive at the river bank\nWould you like to "Wait" for a boat or "Swim" across the river \n').lower()
    if cross == "wait":
        battle = input('You\'ve arrived at the other side of the island\nA group skeleton attacks you woold you "engage" in battle with them or "run" away.\n')
        if battle == "run":
            print("You hid behind a boulder the skeleton passed you, proceed to the door.")
            entrance = input('You\'ve reach the final path of the game, Choose which door has the hidden treasure. "red" or "blue" or "yellow". \n').lower()
            if entrance == "yellow":
                    print("Congratulations, You've found the hidden treasure. Thanks for playing.")
            elif entrance == "red" or entrance == "blue":
                    print("You opened the wrong door the dragon attacked you, Game over.")
        else:
            print("You pulled out your sword to fight them, after a while a horde of skeletons ambushed you. You died.\nGAME OVER.")
    else:
        print("You reached the middle of the river an alligator ambushed you, Game over.")
else:
    print("You fell into one of the hidden trap door, you're dead. Game over.")
    
