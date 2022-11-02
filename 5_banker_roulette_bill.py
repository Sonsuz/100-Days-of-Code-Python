#bill roulette challenge

import random

user_input = input(
  "Please input names of people in your team. Seperate by comma and then a space. \n Such as: Adam, Eve, Jony \n\n"
)

names_list = user_input.split(", ")

r = random.randint(0, len(names_list) - 1)

payer = names_list[r]

print("Guess who is paying today? \n")

print(f"Congrats!! {payer} is paying for today's bill. Good night!")
