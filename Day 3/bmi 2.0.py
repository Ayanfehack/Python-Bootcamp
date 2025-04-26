height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg "))

# bmi = round(weight / (height ** 2), 2)
bmi = 35 
 
if bmi <= 18.5:
    print(f"your bmi is {bmi}, Hence You are underweight.")
elif bmi <= 25:
    print(f"your bmi is {bmi}, Hence You have a normal weight.")
elif bmi <= 30:
    print(f"your bmi is {bmi}, Hence You are overweight.")
elif bmi <= 35:
    print(f"your bmi is {bmi}, Hence You are obese.")
else:
    print(f"your bmi is {bmi}, Hence You are clinically obese.")