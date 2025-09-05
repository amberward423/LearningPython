#rounds=int(input("How many greetings:"))

#finished_rounds=0

#while finished_rounds<rounds:
    #finished_rounds=finished_rounds+1

#command= input("Enter command:")

#while command!= "stop":
   # command=input("Enter command: ")
   # print("We are free, what should we do, let's " +command)#

#print("Execution stopped explicitly.")

import random
#a= random.randint(1,6)
#b=random.randint(1, 9)
#print (a)

import random
#dice1=dice2=rolls=0

#while (dice1!=6 or dice2!=6):
    #dice1=random.randint(1,6)
    #dice2=random.randint(1,6)
    #rolls=rolls+1
#print(f"Rolled {rolls:d} times.")


#first=1
#while first <=5:
   #second=1
   #while second <=5:
        #print(f"{first}times{second} is {first*second:d}")
        #second=second+1
    #first=first+1

#first=2
#while first <=2:
   # second=1
    #while second <=10:
       # print(f"{first} times {second} is {first*second:d}")
       # second=second+1
    #first=first+1""


#rounds= rounds + 1
#total_rolls= total_rolls + rolls
##"average_rolls= total_rolls / rounds"""


#command= input("Enter command:")

#while command!= "stop":
    #if command=="emergency":
        #break
    #print("We are free, what should we do, let's " + command)  #
   # command=input("Enter command: ")
#print("Execution stopped because of emergency")

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



if username_login == username and password_login == password:
        print("Welcome")