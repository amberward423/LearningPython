#def greet(times):
   # for i in range (times):

    #print("Round"+ str(i+1) + "of greetings")

   # return

#print("This print message is part of the main program and the next is the function call")

#greet(10)

#print("Control has moved back to the main program")




def change():
    city= ("Vantaa")

    print("At the end of the function: " + city)

    return

city= "Helsinki"

print("At the beginning in the main program: " + city) # This prints from in the program

change() #Global variable

print("At the end of the main program: " + city)


def print_greet(greeting, times):

    for i in range(times):

        print(greeting + " round " + str(i+1))


    return
a= input("Enter the greeting you wish to be printed: ")
b= int(input("Enter the number of times you wish to make the greeting: "))
print_greet(a,b)

def inventory (items):

    print("Inventory contains the following items: ")

    for item in items:

        print("-" + item)

        backpack.clear()
    return

backpack= ["pen", "pencil", "notebook"]

inventory(backpack)

backpack.append("computer")

print(inventory)

inventory(backpack)

def inventory (nationalities):

    print("You have the following nationalities: ")

    for nationalities in nationalities:

        print("-" +  nationalities)

        return

nationalities = ["American", "Iranian", "Nepalese", "Finnish", "Ukrainian", "Portuguese"]

inventory(nationalities)

print(inventory)




