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
game_images = [rock,paper,scissors]
user_choice = int(input("what do you choose? Type 0 for rock, 1 for paper and 2 for scissors."))
if user_choice<=2 and user_choice >= 0:
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("computer choice")
print(game_images[computer_choice])
if user_choice > 2 and user_choice < 0:
    print("You have typed invalid number.You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you loose")
elif computer_choice > user_choice:
    print("you loose")
elif user_choice > computer_choice:
    print("you loose")
elif user_choice == computer_choice:
    print("It's a tie")