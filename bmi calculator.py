# Python program to illustrate
# how to calculate BMI
print("Welcome to BMI Calculator")
height_inch = float(input("Enter Height in CMs: " ))
weight = float(input("Enter Weight in KGs: "))

#Converting CMs to meters
height = height_inch / 100

def BMI(height, weight):
    bmi = weight / (height ** 2)
    return bmi

# calling the BMI function
bmi = BMI(height, weight)
print("The BMI is {:.15f} So ".format(bmi), end='')

# Conditions to find out BMI category
if (bmi < 18.5):
    print("Underweight")

elif (bmi >= 18.5 and bmi < 24.9):
    print("Healthy")

elif (bmi >= 24.9 and bmi < 30):
    print("Overweight")

elif (bmi >= 30):
    print("Suffering from Obesity")