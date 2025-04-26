import random
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

print("Welcome to the Rock, Paper, Scissors Game.")
pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

random_number = random.randint(0, 2)
computer = print(f"Computer chooses {random_number}")

if pick == 0:
    print(rock)
    if random_number == 0:
        print(rock)
        print("It's a draw, Try Again.")
    elif random_number == 1:
        print(paper)
        print("You lose😢😢, Paper beats rock. Try Again.")
    else:
        print(scissors)
        print("Rock beats Scissors, Congratulation, YOU WIN🥳🥳.")
if pick == 1:
    print(paper)
    if random_number == 0:
        print(rock)
        print("Paper beats rock, Congratulation, YOU WIN🥳🥳.")
    elif random_number == 1:
        print(paper)
        print("It's a draw. Try Again.")
    else:
        print(scissors)
        print("You lose😢😢, Scissors beats Paper. Try Again.")
if pick == 2:
    print(scissors)
    if random_number == 0:
        print(rock)
        print("You lose😢😢, Rock beats Scissors. Try Again.")
    elif random_number == 1:
        print(paper)
        print("Scissors beats Paper, Congratulation, YOU WIN🥳🥳.")
    else:
        print(scissors)
        print("It's a draw, Try Again.")
else:
    print("Invalid number, Pick from 0 - 2. THANK YOU.")