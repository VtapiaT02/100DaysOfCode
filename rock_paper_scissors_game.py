import random

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

options = [rock, paper, scissors]

computer_choice = random.choice(options)

user_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user_number < 0 or user_number> 2:
    print("Invalid Option, Try again.")
else:
    user_choice = options[user_number]
    print(f"You chose:\n{user_choice}")
    print(f"Computer chose:\n{computer_choice}")

    if user_choice == paper and computer_choice == scissors:
        print("You Lose")
    elif user_choice == rock and computer_choice == paper:
        print("You Lose")
    elif user_choice == scissors and computer_choice == rock:
        print("You Lose")
    elif user_choice == computer_choice:
        print("It's a Draw")
    else:
        print("You Win")
