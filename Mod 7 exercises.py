#1
seasons=("Spring", "Summer","Fall", "Winter")
month=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
month_num= int(input("Enter the month number (1-12): "))
season= month[month_num -1]
print(f"Month number {month_num} is  the season of {season} ")


#2


user = input("Enter a new name: ")
names=[]
while names != "":
    names.append(user)
    user = input("Enter a name: ")
for user in names:
    print(names)

    if user in names:
        print(names)
else:
    print("All Done. ")
break



#3

