import random

# Heads or Tails
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")


# Who's Paying
names_string = input("Give me everybody's names, seperated by a comma.\n=> ")
names = names_string.split(', ')
# num_items = len(names)
# random_choice = random.randint(0, len(names) - 1)
# person_who_will_pay = names[random_choice]
person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to buy the meal today!")


# Treasure Map
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n=> ")

horizonal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizonal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")


# Rock Paper Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n=> "))
print(f"\n\nYou chose:\n{choice[user_choice]}\n\n")

if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number, you lose!")

computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{choice[computer_choice]}\n\n")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
else:
    print("It's a draw")
