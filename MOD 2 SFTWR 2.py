class Dog:
    def __init__ (self, name, birth_year, sound= "Woof woof"):
        self.name = name

        self.birth_year = birth_year

        self.sound = sound

    def bark (self, time):

        for i in range(time):

            print(self.name +" barks "+ self.sound)

            return
class Hotel:
    def __init__ (self):

        self.dogs = []

    def dog_checkin(self,dog):

        self.dogs.append(dog)

        print(dog.name + "dog checkin")

        return

    def dog_checkout(self, dog):

        self.dogs.remove(dog)

        print(dog.name + " dog checkout ")

        return

    def greet_dog(self):

        for dog in self.dogs:

            dog.bark(2)


dog1= Dog("Dolly", 2022)
dog2= Dog("Royalty", 2020)
dog3= Dog("Melvin", 2023)

hotel= Hotel()
hotel.dog_checkin (dog1)
hotel.dog_checkin (dog2)
hotel.dog_checkin (dog3)
hotel.greet_dog()
hotel.dog_checkout (dog2)
hotel.dog_checkout (dog3)
hotel.greet_dog()


#### Class example ####

class Student:
    def __init__(self, name):
        self.name = name
class Teacher:
    def __init__ (self):
       self.students=[]

    def add_student (self, student):

        self.students.append(student)

        print(student.name + " is present.")

        return

    def student_leaves (self, student):

        self.students.remove(student)

        print(student.name + " is not present any more.")

        return

    def attendance (self,student):
        for i in range(student):
            print(self.students)
        return

student1= Student("Amber")
student2 = Student("Radin")
student3 = Student("Ana")
teacher= Teacher()
teacher.add_student(student1)
teacher.add_student(student2)
teacher.add_student(student3)
teacher.student_leaves(student3)

