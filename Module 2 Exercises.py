from math import pi

user1 = input("Enter your name:")
print("Nice to meet you," +user1+  "!")

radius = int(input("What is the radius of a circle?"))
area = pi * radius**2
print ( "The area of the circle is:,", float(area ))

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

integer1 = int(input("Enter the first number:"))
integer2 = int(input("Enter the second number:"))
integer3 = int(input("Enter the final number:"))
sum = integer1+integer2+integer3
product = integer1*integer2*integer3
average = sum/3
print("The sum of the numbers entered is:,", int(sum))
print("The product of the numbers entered is:,", int(product))
print("The average of the numbers entered is:," , int(average))