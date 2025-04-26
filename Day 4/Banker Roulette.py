names_string = input("Give me everybody's names, seperated by a comma. \n")
names = names_string.split(", ")

import random

length_name = len(names)
random_name = random.randint(0, length_name - 1)
selected_name = (names[random_name])
print(f"{selected_name} is going to pay for the meal today.")

