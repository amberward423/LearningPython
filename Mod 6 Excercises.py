#1
#Struggled here so I referenced https://www.geeksforgeeks.org/python/args-kwargs-python/
#I also got the recommendation to use args from ChatGPT
#I DID NOT copy any cope from ChatGPT
import random

num_rolled = random.randrange(1, 7)
def dice_roll(*args):
    print("Roll the dice")
    for arg in args:
        print(arg)
    return dice_roll(args)
print("You rolled a " ,num_rolled)
for num_rolled in random.randrange(1,7):
    print("You rolled a ", num_rolled)
else:
    print("You rolled a ", num_rolled, "roll again please")

def dice_roll():
    print("Roll the dice")
    num_rolled = random.randrange(1, 7)
    return num_rolled

#2

import random

user = int(input("Enter a number of sides for your dice: "))
num_rolled = random.randrange(user)

def dice_roll(sides):
    user=int(input("Enter a number of sides for your dice: "))
    print("You rolled a " ,num_rolled)

dice_roll("sides")
for num_rolled in random.randrange(user):
    print("You rolled a ", num_rolled)
else:
    print("You rolled a ", num_rolled, "roll again please")

dice_roll("sides")

#3
## Image used for conversion https://www.lemonsforlulu.com/cooking-conversions/liters-to-gallons/
gallons = int(input("Enter an amount of gas in gallons: "))
liter= gallons*3.79
def gas():
    gallons = int(input("Enter an amount of gas in gallons: "))
    liter= gallons*3.79
    return
print("The amount of gas in liters is ", liter, "L")
if gallons <1:
    break
else:
    print("The amount of gas in liters is ", liter, "L")

#4
num = ["1", "2", "3", "4", "5"]
sum = 1 + 2 + 3 + 4 + 5

def integers(num):
    print("The sum of the integers is ", sum)

integers(num)

#5

num = ["1", "2", "3", "4", "5"]


def integers(num):
    num = ["1", "2", "3", "4", "5"]
    for num in range(1, 6, 2):
        print(num)


def integers(num):
    num = ["1", "2", "3", "4", "5"]
    for num in range(1, 6):
        print(num)



#6






