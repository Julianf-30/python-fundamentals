greeting = "Hello"
name = "Julian"
print(greeting, name)


message = greeting + ", " + name + "."
print(message)

third_letter = greeting[3] 
print(third_letter)

word="ultramicroscopicsilicovolcanoconiosis"
eigthteenth_letter = word[17]
print(eigthteenth_letter)
print(word[-3]) #third to last letter
print(word[-5:]) #last five letters
print(word[:-2]) #all the letters except for last two
print(len(word)) #length of the string
print(word[::2]) #every second letter
print(word[::-3]) #Every third letter but reversed

#Built in Functions
Country="Singapore"
length_of_word = print(len(Country))
phrase = "SpOngEBOB"
print("\nUppercase:", phrase.upper())
print("\nlowercase:", phrase.lower())

#Find and replace 
sentence = "James likes online poker"
new_sentence = sentence.replace("online poker", "hockey")
print(sentence)
print(new_sentence)

#Formatted Strings

name="Julian"
age=14
city="tewksbury"

print(f"Hello, my name is {name}. I am {age} years old and live in {city}.")
 
 
#f-strings can do math and function calls inside {}

print(f"next year, I'll be {age+1}. My name in uppercase is {name.upper()}")


#Challenge 1: Favorite Quote 

quote = input("What is your favorite quote?: ")
print("Your quote is", len(quote), "characters long")

#Challenge 2
first_name =input("What is your first name?: ")
last_name= input("What is your last name?: ")
print("You are", last_name,",", first_name)

#Challenge 3
word=input("Word?: ")
print("Your word is: ", word.upper(), "\n Lowercase: ", word.lower(), "\n Backwards: ", word[::-1])
