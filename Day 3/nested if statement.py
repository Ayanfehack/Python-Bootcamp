number = int(input("What is your height in cm? "))

if number >= 120:
    print("You are eligible to ride. Proceed to age verification")
    age = int(input("How old are you? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Your gate fee is $7. THANK YOU")
    else:
        print("Your gate fee is $12. THANK YOU")
else:
    print("Sorry, come back when you're taller.")
