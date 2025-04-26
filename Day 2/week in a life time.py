age = input("What is your current age: ")
max_age = 90
numbers_of_years_left = int(max_age) - int(age)
day_year = 365
week_year = 52
month_year = 12

days_left = numbers_of_years_left * day_year
weeks_left = numbers_of_years_left * week_year
months_left = numbers_of_years_left * month_year
print(f"You have {days_left}  days, {weeks_left}  weeks, and {months_left}  months left")
