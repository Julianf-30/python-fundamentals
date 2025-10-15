# Conditionals in Python 
#comparison operators: ==, !=, <, >, <=, >=
#logical operators: and, or, not
#control flow: if, elif, else

print(3 == 2)
print (3 != 2)
print( "Hello" == "Hi")

#if 
num = 12 
if num == 10:
    print("Your number is equal to 10")

#If else
num2 = 13 
if num2 <= 12:
    print("Your number is less than 12")
else:
    print("Your number is greater than 12")

#if elif else 
temperature = 93
if temperature > 80:
    print("It's hot!")
elif temperature >= 60:
    print("It's nice out")
else:
    print("It's cold")

x= 2 
y=20 

if x ==y: 
    print("X is equal to y")
elif x > y: 
    print("X is greater than y")
elif x < y: 
    print("X is less than Y")
else: 
    print("Error")

#logical operator: and 
# Both sides of the 'and' must be true, otherwise it's false

age = 16 
has_permission = True 

if age >= 17 and has_permission:
    print("You can drive")
else: 
    print("No can do pal")

# Using 'or' and 'not' 
day = "sunday"
if day == "Saturday" or day == "Sunday":
    print("Its the weekend")
else: 
    print("It's a weekday")

    if day is not "Monday": 
        print("It's not Monday")
    else: 
        print("It's Monday")
    
    #Challenge 1: Even or Odd 
number = int(input("Can I have a number?"))
if number %2 is 0:
    print("Your number is Even")
else:
    print("Your number is odd")

#Challenge 2
password="James is a crashout"
user_password= str(input("Enter your password: "))
if user_password == password: 
    print("Access granted")
else:
    print("Access denied")

#Challenge 3
number_grade = int(input("What was your score? "))
if number_grade >= 90:
    print("You got an A")
elif number_grade >= 80:
    print("You got a B")
elif number_grade >= 70:
    print("You got a C")
elif number_grade >= 60:
    print("You got a D")
else:
    print("You got an F")