#Lists in Python 

#Empty lists
empty_list = []
empty_list.append("Thing")
print(empty_list)

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
animals[0]="babirusa"
print(animals)

animals.append("Glass frog")
print(animals)
animals.insert(3,"Bowerbird")
animals.insert(2,"Camel")
print(animals)

animals.remove("babirusa")
last_animal = animals.pop
print(animals)


animal_to_replace = animals.index("Camel")
print(animal_to_replace)
animals[animal_to_replace] = "Seamonkey"
print(animals)

nums = [3,7,9,1,5,4,6,2,0,8] 

print("Length of list: ", len(nums))
print("Min: ", min(nums))
print("Max:", max(nums))
print("Sum: ", sum(nums))

nums.sort()
print(nums)

animals.sort()
print(animals)
nums.reverse()
print(nums)

if "Cat" in animals: 
    print("Cat is in list")
else:
    print("Cat is not in the list")

a = [1, 2, 3]
copied_list = a.copy()
copied_list.append(4)
print(copied_list)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

print(matrix[0][2])
print(matrix[2][2])

listone =[ 1, 2, 3, 4, 5, 6] 
newnum = int(input("Add a number "))
listone[0] = newnum
print(listone)

shopping = []
shopping.append("Cheese")
shopping.append("Milk")
shopping.append("yogurt")
shopping.insert(2, "ham")
shopping.remove("yogurt")
print(shopping)