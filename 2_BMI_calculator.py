#BMI Calculator - Body Mass Index

#Formula is as follows = weight/ height^2

user_weight = float(input("What is your weight? (kg)  "))
user_height_cm = float(input("What is your height? (cm) "))

user_height_m = user_height_cm / 100

result = user_weight / (user_height_m**2)

print("Your BMI is: " + str(result))

#Reading the BMI data
# <18.5 underweight
# 18.5<x<25 normail
# 25<x<30 overweight
# 30< obese
