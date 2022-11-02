#rock paper scissor game. have fun!!

import random

user_input = int(input("Let's play rocks, papers, scissors. 0 for 🪨, 1 for 📄. 2 for ✂️ \n\n"))

r = random.randint(0, 2)

if r == 0:
  computer_choice = "rock"
elif r == 1:
  computer_choice = "paper"
else:
  computer_choice = "scissor"

if user_input == 0:
  user_choice = "rock"
elif user_input == 1:
  user_choice = "paper"
else:
  user_choice = "scissor"


print(f"You picked: {user_choice}. And the computer picked: {computer_choice}")



if user_input == 0:
  if r == 0:
    print("tie")
  elif r == 1:
    print("computer wins")
  else:
    print("user wins")

elif user_input == 1:
  if r == 0:
    print("user wins")
  elif r == 1:
    print("tie")
  else:
    print("computer wins")

elif user_input == 2:
  if r == 0:
    print("computer wins")
  elif r == 1:
    print("user wins")
  else:
    print("tie")

print ("\n\n Thank you for playing..")
