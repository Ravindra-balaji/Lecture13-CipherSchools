# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sMFjBKOiO_0c5VWU4A2tAZPu_XsbEfsX
"""

name = "Sohail"
age = 20
gender = "MALE"
print(name,age,gender)

num = 9.3
print(pow(num,2))
print(divmod(num,3))
print(round(num))
print(int(num))
print(float("1.23"))
print(num.is_integer())

greeting = "Hello, World!"
print(greeting.lower())
print(greeting.upper())
print(greeting.replace("World!","Sohail!"))
print(greeting.split())
print(greeting.find("or"))

print(len(greeting))

#list
fruits = ["apple","banana","cherry"]
fruits.append("orange")
fruits.extend(["grape","melon"])
print(fruits)

fruits.remove("banana")
print(fruits.pop())  #remove last element
print(fruits)

fruits.sort()
print(fruits)

print(len(fruits))
print(fruits.index("cherry"))
print("apple" in fruits)
fruits





#Tuple
# -- It is immutable
coordinates = (10.0, 20.0)
coordinates

print(coordinates.count(10.0))
print(len(coordinates))

li = list(coordinates)
print(li)

li[1]= "Hi"
print(li)

coordinates = tuple(li)
print(coordinates)

#Dictionary
person = {"name" : "John", "age" : 30}
print(person.keys())
print(person.values())
print(person.items())

print(person.get("name"))
person.update({"age" : 70})
print(person)
person.pop("age")
person

#Set
set1 = {1,2,3,4}

#not allow duplicates
set2 = {1,1,1,1}
print(set2)
print(len(set2))

set2.add(5)
print(set2)
set2.update([6,7,8])
print(set2)
set2.remove(1)
print(set2)

is_active = True
print(int(is_active))
print(bool("Hello!"))
print(is_active and False)

#Conditional statements
age = 20

if(age < 18):
  print("Minor")
elif (age >= 18 and age <= 65):
  print("You are Adult")
else:
  print("Senior")

#Check if even or odd
num = 3

if(num%2 == 0):
  print("Even")
else:
  print("Odd")

#Grade evaluation

score = 85

if(score >= 90):
  print("A")
elif(score >= 80):
  print("B")
elif(score >= 70):
  print("C")
elif(score >= 60):
  print("D")
else:
  print("F")

#Temperature Check

temperature = 30

if(temperature > 30):
  print("It is hot day")
elif temperature >= 20:
  print("It is nice day")
else:
  print("It is cold day")

#Nested conditionals for BMI Calculations
weight = 70
height = 1.75

bmi = weight / (height ** 2)

if bmi < 18.5:
  print("Underweight")
else:
  if bmi < 24.9:
    print("Normal weight")
  else:
    if bmi < 29.9:
      print("Overweight")
    else:
      print("Obesity")

#Age based Discount

age = 70

if age < 18:
  print("Eligible for child discount")
elif age >= 65:
  print("Eligible for senior discount")
else:
  print("Not eligible for discount")



"""Loops"""

#For Loop
for i in range(5):
  print(i)

#Iterating over a List
fruits = ["apple","banana","cherry","Date"]

for fruit in fruits:
  print(fruit)

#Iterating over String

greeting = "Hello"
for char in greeting:
  print(char)

#Iterating over a Dictionary

person = {"name" : "John", "age" : 30, "city" : "new York"}

for key,value in person.items():
  print(f"{key} : {value}")

#Using the 'range()' function with step
for i in range(0,10,2):
  print(i)

#Nested For Loops

for i in range(3):
  for j in range(2):
    print(f"i = {i}, j = {j}")

#Using the 'enumerate()' Function

fruits = ["apple","banana","cherry"]

for index,fruit in enumerate(fruits):
  print(f"Index : {index}, Fruit : {fruit}")

#While loop

count = 0

while count < 5:
  print(count)
  count += 1

#While Loop with break

count = 0

while True:
  if count >= 5:
    break
  print(count)
  count += 1

#While loop with continue

count = 0

while count < 10:
  count += 1
  if count % 2 == 0:
    continue
  print(count)

#Stimulating  a countdown

countdown = 5

while countdown > 0:
  print(countdown)
  countdown -= 1
print("Blast Off!")

#Using a while loop for Validation
password = ""
while len(password) < 8:
  password = input("Enter a password (at least 8 characters) : ")
  if len(password) < 8:
    print("Password must be at least 8 characters long")
print("Password accepted")