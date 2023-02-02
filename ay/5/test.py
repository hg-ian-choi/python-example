############ Average Height ############
import random
student_heights = input("Input a list of student heights\n=> ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
print(student_heights)

# total_height = sum(student_heights)
total_height = 0
for height in student_heights:
    total_height += height

# number_of_students = len(student_heights)
number_of_students = 0
for student in student_heights:
    number_of_students += 1

average_height = round(total_height / number_of_students)
print(average_height)


############ Highest Score ############
student_scores = input("Input a list of student scores\n=> ").split()

for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(student_scores)

heighest_score = 0
for score in student_scores:
    if score > heighest_score:
        heighest_score = score
print(f"The highest score in the class is: {heighest_score}")


############ Adding Evens ############
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

total = 0
for number in range(2, 101, 2):
    total += number
print(total)


############ FizzBuzz ############
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


############ Password Generator ############
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(
    input("How many letters would you like in your password?\n=> "))
nr_symbols = int(input(f"How many symbols would you like?\n=> "))
nr_numbers = int(input(f"How many numbers would you like?\n=> "))

password_list = []

for letter in range(0, nr_letters):
    password_list += random.choice(letters)

for symbol in range(nr_symbols):
    password_list += random.choice(symbols)

for number in range(nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(password)
