name = input("Enter Your Name: ")
print(name)

age = input("Enter your age: ")
print(type(age))

age = int(input("Enter your age: "))
print(type(age))

age_number = int(age)
print("Next year you will be: ", age_number+1)
print(type(age_number))

height= float(input("Enter your height in meters: "))
print("You are", height, "Meters tall")

Favorite_color=input("What is your Favorite Color? ")
print("Your favorite color is: ", Favorite_color)

firstnumber= int(input("Give me a number: "))
secondnumber= int(input("Give me a second number: "))
print(firstnumber + secondnumber )

import math
diameter= int(input("What is the diameter of the circle? "))
radius=diameter/2
print(math.pi*radius**2)

import random 
numberofsides= int(input("How many sides should the die have? "))
print(random.randint(1, numberofsides))

