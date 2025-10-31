class Animal:
    def __init__(self,name,species, sound="animal sound" ):
        self.name= name
        self.sound= sound
        self.species= species

    def print_info(self):
        print(f"The Animal is {self.name}")


class Lion(Animal):
    def __init__(self,name, species, sound="roars"):
        super().__init__(name, species, sound)

    def roar(self, time):
            for i in range(time):
                print(self.name + "roars " + self.sound)

                return
    def print_info(self):
            print(f"The Animal is {self.species}, their name is {self.name} and their sound is {self.sound}")



class Elephant(Animal):
    def __init__(self,name, species, sound="trumpet"):
        self.name= name
        self.species= species
        self.sound= sound
        super().__init__(name, species, sound)

    def trumpets(self, time):
        for i in range(time):
            print(self.name + "trumpets " + self.sound)

            return

    def print_info(self):
        print(f"The Animal is {self.species}, their name is {self.name} and their sound is {self.sound}")


class Snake(Animal):
    def __init__(self,name, species, sound="hiss"):
        self.name= name
        self.species= species
        self.sound= sound
        super().__init__(name, species, sound)

    def hiss(self, time):
            for i in range(time):
                print(self.name + "hisses " + self.sound)

                return
    def print_info(self):
        print(f"The Animal is {self.species}, their name is {self.name} and their sound is {self.sound}")


class Zoo:
    def __init__(self):
        self.zoo= []

    def add_animal(self,animal):
        self.zoo.append(animal)
        return

    def show_all(self):
        for i in self.zoo:
            i.print_info()



a1= Lion("George", "Lion", "ROAR")
a2= Snake("Ryan", "Snake", "hisssss")
a3= Elephant("Ellen", "Elephant", "Trumpet")

zoo= Zoo()
zoo.add_animal(a1)
zoo.add_animal(a2)
zoo.add_animal(a3)
zoo.show_all()

