import keyword

# print all the available keywords in python
#print(f"Keywords in python: {keyword.kwlist}")

# variable - container for a value ( String, Integer, float, boolean)
first_name = "Theerthagiri"
age = 35
iphone_rate = 1200.99
amazing = True
print(
    f"Welcome {first_name}, your age is {age} and you have bought  iphone worth ${iphone_rate} which is {amazing}ly amazing!")

# Typecasting- converting one variable to another variable (str(),int(),float(),bool())
name = "Saraniyaa"
age = 34
gpa = 3.65
is_available = True
print(type(name))
print(float(age))
print(int(gpa))

# input() - prompts user to input function and always returns entered data in string format
# taking multiple inputs from the user
name = input("what is your name:")
print(f"welcome Mr.{name}")

# maths basic
'''
1. +,-,%,*,/
2. math.pi, math.e, math.sqrt, math.floor
'''
import math
#radius = float(input("Enter radius of circle:"))
radius =2
circumference = 2* math.pi * radius
print(f"Circumference of the given radius based circle :{circumference:.2f}")

# if condition - if,else - if,elif,else
#age = int(input("Enter your age: "))
age=2
if age >=18:
    print(F"Your are signed up!")
elif age<0:
    print(f"Please give birth first!")
else:
    print(f"You must be 18+ atleast!")

# logical operators:
'''
1. evaluate multiple conditions (or, and, not)
or - at least one condition must be True
and - both conditions must be True
not - inverts the condition (not False, not True)
'''

# String methods:
name = "giri"
#result = len(name)
#result = name.find("i")
#result = name.rfind("i")
#result = name.capitalize()
#result = name.upper()
#result = name.lower()
#result = name.isalpha()
#result = name.isdigit()
result = name.replace("i","u")
print(f"result is: {result}")
#print(help(str))

# for loops - execute fixed no of times/  iterate over range, string, sequence etc.
for x in range (1,2):
    print (x)

# collection - single variable used to store multiple values
'''
List =[] - ordered and changeable, duplicates OK
Set = {} - unordered and immutable, but ADD / REMOVE Ok. NO duplicates
Tuple = () - ordered and unchangeable. Duplicates OK. FASTER
'''
fruits = ["apple","orange","banana","coco"]
print(fruits)
print(dir(fruits))
'''
append , remove, insert, sort(), reverse(), clear
'''