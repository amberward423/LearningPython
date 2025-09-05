#1

first = 1
while first <= 1000:
    second = 3
    while second <= 3:
        print(f"{first} divided by {second} is {first / second}")
        second = second + 1
    first = first + 1

# I based this on the example we learned in class with Mr. Kirpal
#Singh, K. (2025) "In-class example." Metropolia University. (2025)

#2
inches= int(input("Enter a value in inches: "))
centimeters= inches * 2.54
if inches > 0:
    print("Your converted measurement is " , centimeters, "centimeters")
else:
    print("Bye")

#3
number = input("Enter a number: ")
while number!= "stop":
    if number== "":
        break
    print(number)
    number = input("Enter another number: ")

#For this problem, I based this code on the example in chapter 4. Here is the citation:
#Vesavvo, S. (2025). PYTHON_OHJELMISTOTEEMA/English/04_While_Loops.MD at main · Vesavvo/Python_ohjelmistoteema. GitHub. https://github.com/vesavvo/Python_Ohjelmistoteema/blob/main/English/04_While_Loops.md
#4

print("Let's play a game! Good luck!")

import random

number = random.randrange(1,11,10)

guess = int(input("Guess the number:"))

while  guess < number:
    print("Too low")
    player_2= int(input("Guess again"))
    if guess == number:
       print("Correct")


if guess > number:
    print("Too high")
    player_2 = int(input("Guess again"))

    if guess == number:
       print("Correct")


elif guess == number:
    print("Correct")

##Chegg. (2025). Citation Machine. Citation Machine, a Chegg service. https://www.citationmachine.net/
##Python Software Foundation. (2025). Random - generate pseudo-random numbers. Python documentation. https://docs.python.org/3/library/random.html

#5

username = "python"
password = "rules"

username_login = input("Enter your username: ").lower
password_login = input(" Enter your password: ").lower

while username_login != username:
    username_login = input("Enter your username: ")
    username_login = input("Enter your username: ")
    username_login = input("Enter your username: ")
    print("Access Denied")


if password_login != password:
    password_login = input(" Enter your password: ")
    password_login = input(" Enter your password: ")
    password_login = input(" Enter your password: ")
    print("Access Denied")



elif username_login == username and password_login == password:
        print("Welcome")


#6
print("A square houses a circle that is just big enough to fit inside the edges of the square. We are testing how many points fall inside the circle because this correlates directly to the area of the square. ")
