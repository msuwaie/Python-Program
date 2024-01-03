# input from user height and weight

height = float(input("Enter your height: "))
weight = float(input("Enter your weight "))

# calculting bmi
bmi = (weight/(height*height))*10000
formatted_bmi = "{:.2f}".format(bmi)

# bmi <= 18.5 , underweight
if bmi <= 18.5:
  print("BMI = "+ formatted_bmi + ", Underweight")

# bmi between 18.5 and 24.9 , Normal underweight
elif bmi > 18.5 and bmi <= 24.9:
  print("BMI = " + formatted_bmi + ", Normal weight")

# bmi between 25 and 29.9 , Overweight
elif bmi >= 25 and bmi <= 29.9:
  print("BMI = " + formatted_bmi + ", Overweight")
# bmi 30 or more , Obesity
else:
  print("BMI = " + formatted_bmi + ", Obesity")
