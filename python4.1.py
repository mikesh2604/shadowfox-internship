#to determine the BMI

height=float(input("Enter height in meters:"))
weight=float(input("Enter weight in kilograms:"))

BMI= weight/(height **2)

if BMI >=30:
  category="obesity"
elif 25 < BMI < 29:
  category="Overweight"
elif 18.5 < BMI < 25:
  category="Normal"
elif BMI <= 18.5:
  category="Underweight"

print("BMI Category:",category)
