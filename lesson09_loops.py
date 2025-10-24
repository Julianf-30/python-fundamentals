#Loops in pyton
#Represent a block of code until they hit a limit or condition
#They exist to save us trom typing the same line 500 times
#Python gives us for-loops and while-loops

#For loops repeat for each element in a sequence (Like a list or string) 

animals = ["Lamb", "Sheep", "Cow", "Goose", "Donkey"] 

import time
for animal in animals:
    print("Now petting:", animal)
    time.sleep(1.5)

    if animal == "Sheep":
         print("Hi Sheep")
print("Now I have pet all the animals")

for i in range(5):
     print("Counting", i )

#Use start, step, step with range()

for i in range(2, 11, 2):
     print("Even numbers:", i )