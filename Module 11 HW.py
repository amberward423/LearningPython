"Problem One"
class Publication:
    def __init__(self,name):
        self.name= name

class Book(Publication):
    def __init__(self,author,name, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_info(self):
        print(f'The publication is {self.name} and the author is {self.author} and the page count is {self.page_count}.')

class Magazine(Publication):
    def __init__(self, chief_editor,name):
        self.chief_editor= chief_editor
        super().__init__(name)


    def print_info(self):
        print(f'The publication is {self.name} and the chief editor is {self.chief_editor} .')


a = Book("Rosa Liksom", "Compartment No. 6", 192)
b= Magazine("Aki Hyyppä","Donald Duck")

a.print_info()
b.print_info()

"Problem 2"

class Car():

    def __init__ (self,plate_number,max_speed,curr_speed,t_dist):
        self.plate_number = plate_number
        self.max_speed = max_speed
        self.curr_speed = curr_speed
        self.t_dist=t_dist

    def print_info(self):
        print(f"This car has a registration number of {self.plate_number}, "
              f"a max speed of {self.max_speed} km/hr, "
              f"and a travelled distance of {self.t_dist}.")

    def drive(self, hours,curr_speed,t_dist):
        super().__init__(curr_speed,t_dist)
        self.hours = hours
        t_dist= curr_speed * hours


        print(f"Car One has a registration number of {self.plate_number}, "
          f"a max speed of {self.max_speed} km/hr, "
          f"a current speed of {self.curr_speed} km/hr, "
          f"and a travelled distance of {self.t_dist}.km")

class Electric(Car):
    def __init__(self,plate_number,max_speed,batt_capat,curr_speed, t_dist):
        super().__init__(plate_number,max_speed,curr_speed,t_dist)
        self.batt_capat = batt_capat

    def print_info(self):
        print(f"This car has a registration number of {self.plate_number}, "
              f"a max speed of {self.max_speed} km/hr, "
              f"a current speed of {self.curr_speed} km/hr, "
              f"and a travelled distance of {self.t_dist}.It also has a battery capacity of {self.batt_capat} kWh.")



class Gasoline(Car):
    def __init__(self,plate_number, max_speed, curr_speed, tank_vol,t_dist):
        super().__init__(plate_number, max_speed, curr_speed,t_dist)
        self.tank_vol= tank_vol

    def print_info(self):
        print(f"This car has a registration number of {self.plate_number}, "
              f"a max speed of {self.max_speed} km/hr, "
              f"a current speed of {self.curr_speed} km/hr, "
              f"and a travelled distance of {self.t_dist}.It also has a tank volume of {self.tank_vol} l.")



c = Electric("ABC-123",180, 52.5,56,0)
d = Gasoline("ACD-123",165, 32.3,56,0)
c.drive(3,56,100)
d.drive(3,56,100)

c.print_info()
d.print_info()
