class Dog:
    created= 0
    def __init__(self, name, birth_year, sound= "woof woof"):
        self.name= name
        self.birth_year= birth_year
        self.sound = sound
        Dog.created = Dog.created + 1

    def bark(self, times):
        for i in range(times):
            print(self.sound)
            return



#main program
dog1= Dog("Bubbles", 2022)
dog2= Dog("Blossom", 2010, "yip, yip, yip")


print(f"First dog is named {dog1.name}")
print(f"Second dog is named {dog2.name}")


dog1.bark(3)
dog2.bark(5)

print(f"{Dog.created} dogs have been created. ")

# Class exercise

class Car():

    def __init__ (self,brand, color, mileage = 0,fuel= 100):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.fuel = fuel

    def drive(self, distance):
        fuel_needed = distance /2
        self.mileage += distance
        if self.fuel < fuel_needed:
            print("You do not have enough fuel.")

        else:
            self.mileage += fuel_needed
            self.fuel -= fuel_needed
            print(f"{self.mileage }")

        print(f" {self.brand} has driven {self.mileage} miles. ")

    def repaint(self,color,new_color, brand):
        self.color = color
        self.new_color= new_color
        self.brand = brand
        print(f" The {self.brand} was {self.color} and has been repainted to {self.new_color}")


car1 = Car("Chevy", "red",)
car2 = Car("Ford F 150", "red")

car1.drive(50)
car2.drive(60)

car1.repaint("red", "grey", "Chevy")
car2.repaint("red", "green", "Ford F 150")


