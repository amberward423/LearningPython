import random
class Car:
    def __init__(self,reg,curr_speed= 0,t_dist= 0 ):
        self.reg= reg
        self.curr_speed= curr_speed
        self.t_dist= t_dist

    def print_info(self):
        print(f"Car One has a registration number of {self.reg}, "
              f"a max speed of {self.max_speed} km/hr, "
              f"a current speed of {self.curr_speed }, "
              f"and a travelled distance of {self.t_dist}.")

    def accelerate(self, change_speed, curr_speed,new_speed):
        self.new_speed= new_speed
        self.__change_speed= change_speed
        if change_speed >= 1:
            new_speed = change_speed + curr_speed
        elif change_speed <= 1:
            new_speed = curr_speed - change_speed

        print(f"Car One has a registration number of {self.reg}, "
          f"a max speed of {self.max_speed} km/hr, "
          f"a current speed of {self.new_speed} km/hr, "
          f"and a travelled distance of {self.t_dist}.")

    def drive(self, hours, t_dist):
        self.hours = hours
        self.t_dist = t_dist
        t_dist = self.curr_speed * hours

        print(f"Car One has a registration number of {self.reg}, "
          f"a max speed of {self.max_speed} km/hr, "
          f"a current speed of {self.new_speed} km/hr, "
          f"and a travelled distance of {self.t_dist}.km")

    def max(self):
        self.max_speed = random.randrange(100, 200)
        return random.randrange(self.max_speed)

#I am completely lost in terms of question 4, I do not understand how to program the race. I have worked on this for a while and googled and you-tubed, but I cannot solve this.
# Please advise.

# The race class is from Mod 10
class Race:
    def __init__(self,name, kilometers):
        self.name= name
        self.kilometers= kilometers

    def print_info(self):
        pass

    def hour_passes(self, hours, t_dist):
        self.hours= hours
        self.t_dist=t_dist
        super(Car).print_info(hours,t_dist)
## having trouble with the super statement








cars=[]
car1= Car("ABC-1",147,  0)
car2= Car("ABC-2",147,  0)
car3= Car("ABC-3",147,  0)
car4= Car("ABC-4",147,  0)
car5= Car("ABC-5",147,  0)
car6= Car("ABC-6",147,  0)
car7= Car("ABC-7",147,  0)
car8= Car("ABC-8",147,  0)
car9= Car("ABC-9",147,  0)
car10= Car("ABC-10",147,  0)
Car.max(car1)
Car.max(car2)
Car.max(car3)
Car.max(car4)
Car.max(car5)
Car.max(car6)
Car.max(car7)
Car.max(car8)
Car.max(car9)
Car.max(car10)
print(car1)
print(car2)
print(car3)
print(car4)
print(car5)
print(car6)
print(car7)
print(car8)
print(car9)
print(car10)










