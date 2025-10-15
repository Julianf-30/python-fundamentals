#Lists in Python 
my_list= [1,2,3]

animals=["penguin", "Koala", "Dugong"]
numbers = ["1", "2", "5",]
mixed= [True, 42, "Blue", 8.4]

print(animals)
print(numbers)
print(mixed)

 #First element
print(animals[0])

#Second Element
print(animals[1])

#Last element 
print(animals[-1])

#modyfing lists
animals[0]= "babirusa"
print(animals)

animals.append("Glass frog")
print(animals)
animals.insert(3,"Bowerbird")
animals.insert(2,"Camel")
print(animals)

animals.remove("babirusa")
last_animal = animals.pop
print(animals)

animals.remove("Babirusa")
