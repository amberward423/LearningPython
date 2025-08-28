##user1= int(input("Enter an integer"))
##if user1<0 :
##    print(user1*-1)
##else:
##   print(user1)
##
##age=int(input("How old are you?"))

##if 15 <= age < 18:
    #weight= float(input("How much do you weigh? "))

##if age >= 18 or age >= 15 and weight >= 55 :
    #print("You can use the medicine.")

##else:
    #print("You cannot use the medicine.")

#name = input("Please tell me your name:") .lower()

#if name != "matti":
   #print("Next Please!")

#else:
    #print("Next Please!")

#print ("Goodbye!")

#age= int(input("How old are you?"))

#if age >= 65 :
    #print("You are retired.")
#elif age>= 18:
    #print("You are working age.")
#elif age >7:
    #print("You are still in school.")
#else:
    #print("You are a small child.")

#number = int(input("Please type a number:"))

#if number > 0:
   # if number % 2 ==0 :
        #print("Number is even.")
    #print("Number is odd.")
#else:
   # print("Number is negative or zero.")

hourly_wage = float(input("hourlywage: "))
hours_worked = float(input("hoursworked: "))
day_of_the_week= input("dayoftheweek: ")
daily_wage = hourly_wage * hours_worked

if day_of_the_week == "Sunday":
   print(f"daily wage: {hourly_wage*hours_worked*2}")

else:
    print(f"daily wage: {hourly_wage* hours_worked}")

