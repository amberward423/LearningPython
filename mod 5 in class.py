names=["Viivi", "Ahmed", "Pekka","Olga", "Mary"]

#print (names[1])
#print (names[1:4])
#print(names[2:])
#print(names)

#print (len(names))

names.append("Matti")

print(names)

names.remove("Pekka")
names.remove("Matti")

print(names)

names.insert(2, "Teppo")

print(names)

names2=["Allu", "Niini"]


names.extend(names)
print (names)

olga=names.index("Olga")
print(olga)

# print("Matti found again")

if "Matti" in names:
    print("Matti was found.")
else:
    print("Matti was not found.")
#if (value) in (data structure)

names.append("Matti")
print(names)

if "Matti" in names:
    print("Matti was found.")
else:
    print("Matti was not found.")

print(names)

names.sort()
#By default it sorts letters alphabetically and numbers from least to greatest

print(names)

names.sort(reverse=True) #this just simply reverses the letters and numbers

print(names)

for n in names:
    print("Hello",n)
