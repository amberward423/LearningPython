#1
user_1= int(input("What is the length of the zander you've caught?"))
zander=42-user_1

if user_1 <42:
    print("Please release the zander, it is too small. The zander is ", +zander ,"cm below the accepted limit of 42 cm " )
else:
    print ("Enjoy your catch!")
#2



user_2= input("What is the cabin class of your cabin")

if user_2==a:
    print("Your cabin is an ",{a}, "it has a window")

elif user_2 == b:
    print("Your cabin is an ", {b})

elif user_2==c:
    print("Your cabin is an ", {c})

else:
    print("Your cabin is " , {lux})


#3
gen_a = 'Female'
gen_b = 'Male'
gender= input("What is your biological gender?: ")
hg= int(input("What is your hemoglobin value?: "))

if (117 >  gen_a > 155 or 134 > gen_b > 167):

    print("Your hemoglobin level is high.")

if (117 < gen_a < 155 or  134 < gen_b <167):

    print("Your hemoglobin is low")
else:
    if (117 ==  gen_a == 155 and 134 == gen_b== 167) :

        print("Your hemoglobin level is normal.")


#4

user_3 = int(input("Enter a year:"))
leap_year=user_3/4

if user_3/100 and user_3/400:
    print("This", user_3 ,"is a leap year")

if leap_year:=user_3/4:

    print("This", user_3, "is a leap year")
else:
    print("This year is not a leap year")