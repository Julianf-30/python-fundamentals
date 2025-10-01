#Python libraries are ike repositories to add to your code

#MATH LIBRARY

import math
print("\n--- Math Library ---\n")

print("square root:", math.sqrt(49))
print("Round Up:", math.ceil(4.001))
print("Round Down:", math.floor(5.999))
print("Power: ", math.pow(2, 5))
print("Pi: ", math.pi)

# RANDOM LIBRARY

seed= 86734

part1=seed/150
part2=part1*seed-450
part3=part2/part1*.1
part4=math.floor(part3)
part5=part4+0.2
print(part5)

number=54
step1=number/2
step2=step1+5
step3=step2 -20
step4=step3-5
print(step4)


import random 

# metods: 
print("Random Integer: ", random.randint(1, 1000000))

print(random.random())

mylist= ["Eggs","Keys","Chicken","Salsa",]
print(random.choice(mylist))
random.shuffle(mylist)
print(mylist)

#Challenge 1: Circle Area with Math Library

radius=7
circle_area=math.pi * math.exp(radius, 2)
print(math.floor(circle_area))

#Challenge 2

print("Die Roll: ", random.randint(1, 6))