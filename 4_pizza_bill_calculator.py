#Pizza bill calculator

bill = 0

size = input("Please input pizza size you would like? \n S for small, M for medium, L for large. \n")

if size == "S" or size == "s":
  bill += 15
elif size == "M" or size == "m":
  bill += 20
elif size == "L" or size == "l":
  bill +=25

pep = input("Would you like to add any pepporoni? Y or N \n")
if pep == "Y" or pep == "y":
  if size == "S" or size =="s":
    bill += 2
  else:
    bill += 3
else:
  bill = bill

chs = input("Would you like to add any cheese on top? Y or N \n")
if chs == "Y" or chs == "y":
  bill += 1
else:
  bill = bill

tax = 0.10

result = bill + bill*tax
print(f"Your final bill is : {result}. Have a great day!")
