# Loops in pyton
# Represent a block of code until they hit a limit or condition
# They exist to save us trom typing the same line 500 times
# Python gives us for-loops and while-loops

# For loops repeat for each element in a sequence (Like a list or string) 

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

# Use start, step, step with range()

for i in range(2, 11, 2):
     print("Even numbers:", i )

fav_word = "Shenanagin"

letter_list = [] 

for letter in fav_word:
     print(letter, end ="")
     letter_list.append(letter)
     print(letter_list)

print()

#While loops 
import time 
count = 0 

while count < 5:
     print(f"looping. We are on loop #{count}.")
     count += 1 
     time.sleep(0.5)

print("We have escaped the loop fr")

user_input = ""



while user_input != "exit":
     user_input = input("Type exit to escape: ")
     
while user_input != "exit":
     if user_input =="exit":
          print("Exited")
          break

count = 60 
increment = 1 
while count > 0:
     count -= increment 
     increment += 1
     if count < 0:
          break 
     
     print(count)

import random 
fruits = ["Mango", "Apple", "Banana", "Papaya", "Jackfruit", "Cantelope", "Honeydew"]
count = int(input("How many fruits would you like? "))
for fruit in range(count):
     print("You picked: ", random.choice(fruits))