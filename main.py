# Write your solution below the starter code
# Follow the instructions in the tab to the right

import random

# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")
users_choice = input("Enter your choice (rock, paper, scissors:) ") 
# Make a choice for the computer player
# Get a choice from the user
# Compare the user and computer choice
# Print the right message, based on the choices
choices = ("rock", "paper", "scissors")
computer = (random.choice(choices))
print(f"\nyou chose: {users_choice}, computer chose: {computer}./n")
if users_choice == computer:
  print(f"both users selected {users_choice}.it's a draw ")
elif users_choice == "rock":
  if computer == "scissors":
    print("rock smashes scissors, you win!")
  else:
    print("paper covers rock, computer wins")
elif users_choice == "paper":
  if computer == "scissors":
    print("scissors cut paper, computer wins!")
  else:
    print("paper covers rock, you win")
elif users_choice == "paper":
  if computer == "rock":
    print("paper covers rock, you win! ")
  else:
    print("scissors cut paper, computer wins")
elif  users_choice != "rock, papers, scissors.": 
    print ("you have to enter rock, papers, scissors")
