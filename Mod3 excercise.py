#1
user_1= int(input("What is the length of the zander you've caught?"))
zander=42-user_1

if user_1 <42:
    print("Please release the zander, it is too small. The zander is ", +zander ,"cm below the accepted limit of 42 cm " )
else:
    print ("Enjoy your catch!")
#2
a = "Above car deck cabin that has a window"
b = "Windowless cabin that is above the car deck"
c ="Windowless cabin that is below the car deck"
lux= "Upper deck cabin with a balcony"


user_2= (input("What is the cabin class of your cabin ")). lower()

if user_2=="a":
    print("Your cabin is an ",a)

elif user_2 == "b":
    print("Your cabin is an ", b)

elif user_2=="c":
    print("Your cabin is ", c)

elif user_2==" lux":

    print("Your cabin is " , lux)

else:
    print("Invalid cabin class")

#3
# I struggled with this code and cannot figure out how to make my statements have an effect
gen_a="female"
gen_b="male"
gender= input("What is your biological gender?: ")
hg= int(input("What is your hemoglobin value?: "))


if (117 <= gen_a or gen_a <= 155) and (134 <= gen_b or gen_b <= 167):
   pass
else:
   print("Your hemoglobin level is high.")


if 117 < gen_a < 155 or 134 < gen_b and gen_b < 167:


   print("Your hemoglobin is low")
else:
   if 117 ==  gen_a == 155 and 134 == gen_b== 167:


       print("Your hemoglobin level is normal.")


#4

year= int(input("Enter a year:"))

while int(year/4):
    print("This year is a leap year")

if year/100 and year/400:
    print("This year is a leap year")
else:
    print("This year is not a leap year")

