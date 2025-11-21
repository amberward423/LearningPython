# Example 1
class Food:
    def __init__(self,name,num_of_calories):
        self.name = name
        self.num_of_calories = num_of_calories


    def print_info(self):
        print(f"{self.name} has {self.num_of_calories} calories.")



class Fruit(Food):
    def __init__(self,name,calories,is_sweet):
        self.is_sweet = is_sweet
        super().__init__(name, calories)
        #is_sweet is a boolean value

    def print_info(self):
        super().print_info()
        print(f"Sweet:{"Yes" if self.is_sweet else "No"}")

#Using a boolean as an attribute:
# print(f"Sweet:{"Yes" if self.is_sweet else "No"}")#
#same thing for the veggie class



class Veggie(Food):
    def __init__(self,name, calories,is_leafy):
        self.is_leafy = is_leafy
        super().__init__(name, calories)

    def print_info(self):
        super().print_info()
        print(f"Leafy:{"Yes" if self.is_leafy else "No"}")


#really review this for exam

class Store:
    def __init__ (self):
        self.inventory = {}

# using a dictionary
    #def buy(self,food):
        #self.inventory.update{food}# what I wrote
        #print(food.name + "added to the list.")#
# What Heidi wrote
    def add(self,food_obj):
        self.inventory[food_obj.name.lower()] = food_obj
        # this is how to make a dictionary in a class and add something
        # to the dictionary

    def print_inventory(self):
       print("Available products: ")
       for item in self.inventory.values():
           item.print_info()
    #this is how we show what is in the inventory

    def buy(self, product_name):
        name = product_name.lower()
        #checks to see if it is in the inventory while you are shopping
        if name in self.inventory:
            return self.inventory[name]
        else:
            return None

class Smoothie:
    def __init__(self,name, ingredients):
        self.name = name
        self.ingredients = ingredients
        total = 0

        for item in ingredients:
            total += item.calories

        self.total_calories = total


    def smoothie_info(self):
        print(f"Smoothie name: {self.name}. ")
        print(f"Ingredients: ")
        for item in self.ingredients:
            print("-", item.name)
            print(f"Total calories : {self.total_calories} ")


h = Fruit('apple',40, True)
h2= Fruit('raspberries', 30, True)
i = Veggie('kale', 20, True)
i2= Veggie('spinach', 25, True)


lidl= Store()
lidl.add(h)
lidl.add(h2)
lidl.add(i)
lidl.add(i2)

lidl.print_inventory()
print(lidl.inventory)

ingredients= []
print('Welcome to Lidl.')
lidl.print_inventory()
while True:
     i = input("Add an ingredient to your smoothie. {empty to finish}")
     if i == "":
         break
product = lidl.buy(i)

if product:
    ingredients.append(product)
    print(f"Added {product.name}")
else:
    print("We don't have it here.")

if len(ingredients) == 0:
    print('No ingredients were found.')

smoothie = Smoothie("razztastic", ingredients)
smoothie.smoothie_info













