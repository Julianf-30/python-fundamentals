def say_hi():
    print("Hi")


def say_bye():
    print("bye")

say_hi()

def express_this(e):
    return e

expression1 = express_this(1+2)
print(expression1)

expression2 = express_this(45*6)
print(expression2)

def greeter(n): 
    return f"HI {n}"

first = greeter("julian")
second = greeter("jjcool")
third = greeter("coolian")

print(first, second, third)

def remainder(a, b):
    return a % b

result = remainder(3, 2)
print(result)

def is_far(distance):
    if distance < 1:
        return "error"  #base case 
    if distance >= 100:
        return "That's far"
    elif distance < 100 and distance > 20:
        return "not too far"
    elif distance <= 20:
        return "That's nearby!"
    

print(is_far(200))
print(is_far(50))
print(is_far(20))
print(is_far(-5000))

def doubler(number, times):
    value = number
    sequence = []
    for i in range(times):
        value = value * 2
        sequence.append(value)
    return sequence 

result = doubler(1, 2)

print(result)
