from math import pi

#1
user1 = input("Enter your name:")
print("Nice to meet you," +user1+  "!")
#2
radius = int(input("What is the radius of a circle?"))
area = pi * radius**2
print ( "The area of the circle is:,", float(area ))
#3
side1= int(input("What is the length of side one of a rectangle?:,"))
side2= int(input("What is the length of side two of a rectangle?:,"))
side3= int(input("What is the width of side three of a rectangle?:,"))
side4= int(input("What is the width of side four of a rectangle?:,"))
perimeter= int (side1 + side2 + side3 + side4)
length = int(side1 * side2)
width = int(side3 * side4)
area= int(length * width)
print ("The perimeter of the rectangle is,", int(perimeter))
print ("The area of the rectangle is," , int(area))
#4
integer1 = int(input("Enter the first number:"))
integer2 = int(input("Enter the second number:"))
integer3 = int(input("Enter the final number:"))
sum = integer1+integer2+integer3
product = integer1*integer2*integer3
average = sum/3
print("The sum of the numbers entered is:,", int(sum))
print("The product of the numbers entered is:,", int(product))
print("The average of the numbers entered is:," , int(average))
#5
talents= int(input("Enter talents: "))
pounds= int(input("Enter pounds: "))
lots= int(input("Enter lots: "))
talents = float(talents*44.0924)
pounds = float(pounds*2.20462)
lots=float(lots*0.0133)
kilograms=talents+pounds
grams= lots
print("Your weight in kilograms is ", {kilograms:10.2} )
print("Your weight in grams is ", {grams:10.2})


#6 used (GeeksforGeeks, S. E. P. L., 2025) for this problem because import random did not work
import random
num1= random.randint(0,9)
num2= random.randint(0,9)
num3= random.randint(0,9)

print("Your random three-number combination is ", (num1),(num2),(num3))

#6 part two
import random
num1= random.randint(1,6)
num2= random.randint(1,6)
num3= random.randint(1,6)
num4= random.randint(1,6)

print("Your random four-number combination is ", (num1),(num2),(num3), (num4))

#Sources
## Chegg. (2025). Citation Machine. Citation Machine, a Chegg service. https://www.citationmachine.net/
##GeeksforGeeks, S. E. P. L. (2025, July 11). Randint() function in Python. https://www.geeksforgeeks.org/python/python-randint-function/