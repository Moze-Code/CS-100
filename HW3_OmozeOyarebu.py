"""
Omoze Oyarebu
CS 100 2023S Section 012
HW 03, February, 2023

"""

#Exercise 1
months = ['January','February','March','April','May','June','July','August','September','October','Novermber','December']
string_search = 'J'

#Looping through the list and checking whether each item's first index contains a J 
for x in months:
    if string_search in x[0]:
        print(x)
print()

#Excerise 2
#traversing from 0 to 99 inclusive and printing numbers divisible by 2 and 5
for x in range(0,100,1):
    if ((x % 2 == 0) and (x % 5 == 0)):
        print(x)
print()

#Excercise 3

#Loop through the horton and print out all occurances of vowels in the order they appear
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"

for x in horton:
    if x in vowels:
        print(x)
print()

#Exercise 4
import math

print("100 factorial is:")
print(math.factorial(100), "\n")

print("log of 1,000,000 of base 2 is:")
print(math.log(1000000,2),"\n")

print("The gcd of 63 and 49 is:")
print(math.gcd(63,49),"\n")

#Exercise 5a
import turtle

#1
#equilateral triangle with side length 100
triangle = turtle.Turtle()
triangle.forward(100)
triangle.left(120)
triangle.forward(100)
triangle.left(120)
triangle.forward(100)
triangle.hideturtle()
triangle.clear()

#2
#Square with side length 100
square = turtle.Turtle()
for x in range(4):
    square.forward(100)
    square.left(90)
square.hideturtle()
square.clear()

#3
#Petagon with side length 100
pentagon = turtle.Turtle()

for x in range(5):
    pentagon.forward(100)
    pentagon.left(72)
pentagon.hideturtle()
pentagon.clear()

#Exercise 5b
#Drawing 4 concentric Circle with increasing raduis of 50 at each loop iteration
circle = turtle.Turtle()
radius = 0

for x in range(4):
    circle.circle(radius + 50)
    circle.penup()
    circle.right(90)
    circle.forward(50)
    circle.left(90)
    circle.pendown()
    radius = radius + 50
circle.hideturtle()




