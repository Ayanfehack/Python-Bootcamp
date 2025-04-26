year = int(input("Which year do you want to check? "))

if (year % 4) == 0:
    if (year % 100) > 0:
        print("It is leap year")
    elif (year % 400) == 0.0:
        print("It's a leap year.")
    else:
        print("It is not a leap year.")
else:
    print("Not a leap year")
     