print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

convert1 = f"{name1}".lower()
convert2 = f"{name2}".lower()

t = f"{convert1 + convert2}".count("t")
r = f"{convert1 + convert2}".count("r")
u = f"{convert1 + convert2}".count("u")
e = f"{convert1 + convert2}".count("e")
true = t + r + u + e

l = f"{convert1 + convert2}".count("l")
o = f"{convert1 + convert2}".count("o")
v = f"{convert1 + convert2}".count("v")
e = f"{convert1 + convert2}".count("e")
love = l + o + v + e
love_score = int(f"{true}{love}")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, You go together like coke and mentos.")
elif love_score > 100:
    print(f"Your score is {love_score},")    
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, You are alright together.")
else:
    print(f"Your score is {love_score}.")
    