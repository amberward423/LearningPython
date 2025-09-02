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
gender=["Male", "Female"]
gender= ("Enter your biological gender: ")
hemoglobin= ("Enter your hemoglobin level: ")

if gender == "Female":
    117 >  hemoglobin > 155
    print("Your hemoglobin is higher than normal levels.")

if gender == "Male":
    134 > hemoglobin > 167
    print("Your hemoglobin is higher than normal levels.")

if gender == "Female":
    117 == hemoglobin == 155
    print("Your hemoglobin is normal.")

if gender == "Male":
    134 == hemoglobin == 167
    print("Your hemoglobin is normal.")

if gender == "Female":
    117 < hemoglobin < 155
    print("Your hemoglobin is lower than normal levels.")

if gender == "Male":
        134 < hemoglobin < 167
        print("Your hemoglobin is lower than normal levels.")

#4

year= int(input("Enter a year:"))

if int(year/4):
    print("This year is a leap year")

else:
    print("This year is not a leap year")

