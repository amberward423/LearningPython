class Car:
    def __init__(self,reg,max_speed,curr_speed= 0,t_dist= 0 ):
        self.reg= reg
        self.max_speed= max_speed
        self.curr_speed= curr_speed
        self.t_dist= t_dist

    def print_info(self):
        print(f"Car One has a registration number of {self.reg}, "
              f"a max speed of {self.max_speed} km/hr, "
              f"a current speed of {self.curr_speed }, "
              f"and a travelled distance of {self.t_dist}.")

    def accelerate(self, change_speed, curr_speed,new_speed):
        self.new_speed= new_speed
        self.change_speed= change_speed
        if change_speed >= 1:
            new_speed = change_speed + curr_speed
        elif change_speed <= 1:
            new_speed = curr_speed - change_speed

        print(f"Car One has a registration number of {self.reg}, "
          f"a max speed of {self.max_speed} km/hr, "
          f"a current speed of {self.new_speed} km/hr, "
          f"and a travelled distance of {self.t_dist}.")

    def drive(self, t_dist, hours, curr_speed):
        self.hours= hours
        t_dist = curr_speed * hours
        print(f"Car One has a registration number of {self.reg}, "
          f"a max speed of {self.max_speed} km/hr, "
          f"a current speed of {self.new_speed} km/hr, "
          f"and a travelled distance of {self.t_dist}.km")









car1= Car("ABC-123", 142, 0, 0 )
car1.print_info()
car1.accelerate(30, 0, 30)
car1.accelerate(70, 0, 70)
car1.accelerate(50, 0, 50)
car1.accelerate(-200, 0, -200)
car1.drive(2000, 1.5, 60)
