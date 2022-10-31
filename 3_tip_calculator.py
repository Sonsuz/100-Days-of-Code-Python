#Tip Calculator

total_amount = float(input("How much is the total cost?  "))

total_people = int(input("How many people are spliting the bill?  "))

tip_percentage = float(input("Tip percentage you would like to give?  ")) * 0.01

result = ((total_amount) / total_people) + (total_amount / total_people) * tip_percentage

print(result)
