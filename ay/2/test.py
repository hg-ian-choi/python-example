# Add Two Number
two_digit_number = input("Type a two digit number: ")
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# BMI Calculator
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / height ** 2
print(int(bmi))


# Your Life in Weeks
age = input("What is your current age?\n=> ")
years = 90 - int(age)
days = years * 365
weeks = years * 52
months = years * 12
print(f"You have {days} days, {weeks} weeks and {months} months")


# Tip Calculator
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?\n=> "))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15?\n=> ")) / 100
people = float(input("How many people to split the bill?\n=> "))
each_pay = (total_bill + total_bill * tip) / people
round_each_pay = round(each_pay, 2)
result = "{:.2f}".format(round_each_pay)
print(f"Each person should pay: {result}")
