#Create base class
class Employee:
    total= 0

    def __init__ (self,name, last_name):
        Employee.total += 1
        # += 1 is a short-cut for addition
        self.number = Employee.total
        self.name= name
        self.last_name= last_name


    def print_info(self):
            print(f' Employee number {self.number} : {self.name}, {self.last_name}')

#subclasses inherited from the base class ; Like when you call a function
class HourlyPaid(Employee):

    def __init__(self, name, last_name, hourly_pay):
        self.hourly_pay = hourly_pay
        super().__init__(name, last_name)
        #super() is the function that calls the upper class

    def print_info(self):
        super().print_info()
        print(f" Hourly pay: {self.hourly_pay} $")

class MonthlyPaid(Employee):
    def __init__(self, name, last_name, monthly_pay):
        self.monthly_pay = monthly_pay
        super().__init__(name, last_name)

    def print_info(self):
        super().print_info()
        print(f" Monthly pay: {self.monthly_pay} $")



# main program
employees= []
emp1= Employee("Viivi", "Virta")
emp2 = Employee("Ahmed", "Habib")
emp3= HourlyPaid("Pekka", "Puro", 14.50)
emp4= MonthlyPaid("Heidi", "Teacher", 6531)
employees.append(emp1)
employees.append(emp2)
employees.append(emp3)
employees.append(emp4)


for e in employees:
    e.print_info()


# New example with two base classes

class Publication:
    total = 0

    def __init__ (self, name):
        self.name= name
        Publication.total += 1

    def print_info(self):
        print(f" Publication name is {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count= page_count
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f" The book is written by {self.author}.")

class Mag(Publication):
    def __init__ (self, chief_editor, name):
     self.chief_editor = chief_editor
     super().__init__(name)
     print(f" The chief editor is {self.chief_editor}.")

    def print_info(self):
        super().print_info()
        print(f" The magazine is written by {self.chief_editor}.")



p1= Publication("Time")
p1.print_info()

p2 = Book("Cat in the hat","Dr.Seuss", 20)
p2.print_info()

p3= Mag("Anna Wintour", "Vogue")
p3.print_info()



## Example number 3
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

