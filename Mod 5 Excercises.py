
### Question 1
import random
num_dice = (input("How many dice would you like to roll?"))

dice_roll_1= random.randrange(1,7)
dice_roll_2= random.randrange(1,7)
sum = dice_roll_1+dice_roll_2

for dice_roll in range(1,7):
    if sum == 1:
        print("The numbers rolled are", dice_roll_1, "and", dice_roll_2)
        print("The sum of the numbers rolled is", sum)
    if sum == 2:
        print("The numbers rolled are", dice_roll_1, "and", dice_roll_2)
        print("The sum of the numbers rolled is", sum)

    if sum == 3:
        print("The numbers rolled are", dice_roll_1, "and", dice_roll_2)
        print("The sum of the numbers rolled is", sum)

    if sum == 4:
        print("The numbers rolled are", dice_roll_1, "and", dice_roll_2)
        print("The sum of the numbers rolled is", sum)
    if sum == 5:
        print("The numbers rolled are", dice_roll_1, "and", dice_roll_2)
        print("The sum of the numbers rolled is", sum)
    if sum == 6:
        print("The numbers rolled are", dice_roll_1, "and", dice_roll_2)
        print("The sum of the numbers rolled is", sum)


### Question 2

##W3 Schools. (n.d.-b). Python List reverse() Method. W3Schools Online Web Tutorials. https://www.w3schools.com/python/ref_list_reverse.asp

numbers = []

user = (input(f"Enter a number (to quit press Enter): "))

while user != "":
    numbers.append(user)
    user= (input(f"Enter another number (to quit press Enter): "))
    if user == "":
        break
numbers.reverse()
print(numbers)



### Question 3

num = int(input("Enter an integer: "))

if num/1 and num/num==1:
     print("This number is a prime number.")

else:
    print("This number is not a prime number.")


### Question 4

user = input("Enter the name of a city: ")
cities=[]
while cities != "":
    cities.append(user)
    user = input("Enter the name of a city: ")
for user in cities:
    print(cities)

    if user in cities:
        print(cities)
else:
    print("All Done. ")
break

















