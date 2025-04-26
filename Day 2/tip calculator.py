print("Welcome to the tip calculator. ")

bill = int(float(input("what was the total bill? $")))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_tip = (bill * tip / 100)

print("Amount of tip to be paid is $" + str(total_tip))

number_of_people = int(input("How many people to split the bill? "))

# total_amount_to_be_paid = round(((bill) + (total_tip)) / (number_of_people), 2)
total_amount_to_be_paid = "{:.2f}".format(((bill) + (total_tip)) / (number_of_people))
total = str(total_amount_to_be_paid)
print("Each person should pay: $" + (total))
# print(type(tip))