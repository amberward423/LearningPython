class Elevator:
    def __init__(self, b_floor_num=0 , t_floor_num=5):
       self.b_floor_num = b_floor_num
       self.t_floor_num = t_floor_num



    def print_info(self):
            super().print_info(b_floor_num=0,t_floor_num=5)


    def go_to_floor(self,new_floor,current_floor, end_floor1, end_floor2):
        self.end_floor1= end_floor1
        self.end_floor2= end_floor2
        self.current_floor= current_floor
        self.new_floor= new_floor
        self.end_floor1 =+ current_floor + new_floor
        self.end_floor2 =+ current_floor - new_floor
        print(input("Enter floor number, please: "))
        super().print_info(b_floor_num=0, t_floor_num=5)

    def floor_up(self,new_floor,current_floor):
        self.end_floor1 = self.end_floor1
        self.new_floor = new_floor
        self.current_floor= current_floor
        print(input("Enter floor number, please: "))
        self.end_floor1= current_floor + new_floor
        print(f"You are now at floor {self.end_floor1}")
        super().print_info(b_floor_num=0, t_floor_num=5)

    def floor_down(self,new_floor,current_floor, end_floor2):
        self.end_floor2 = end_floor2
        self.current_floor= current_floor
        self.new_floor = new_floor
        print(input("Enter floor number, please: "))
        self.end_floor2 =+ current_floor - new_floor
        print(f"You are now at floor {self.end_floor2}")
        super().print_info(b_floor_num=0, t_floor_num=5)


class Building:
    def __init__(self,b_floor_num=0 , t_floor_num=5, e_num= 3):
        self.b_floor_num = b_floor_num
        self.t_floor_num = t_floor_num
        self.e_num= Elevator(e_num)
        self.elevator = []
        super().print_info(b_floor_num=0, t_floor_num=5)

    def run_elevator (self,e_num, dest_floor):
        self.dest_floor= dest_floor
        self.e_num= e_num
        super().print_info(b_floor_num=0, t_floor_num=5)

    def fire_alarm(self):
            for self.e_num in self.elevator:
                self.run_elevator(0,0)



building = Building()
Building.run_elevator(0,0)
Building.fire_alarm(Elevator)
Elevator.floor_down(0,5,0,1)
Elevator.floor_up(0,5,0)
Elevator.go_to_floor(0,5,0,1)



## in testing I got this error, and I am unsure of what to do moving forward.
# I have sought help from friends, google, and geeksforgeeks and I am unable to figure this out
# /Users/amberward/PycharmProjects/LearningPython/.venv/bin/python /Users/amberward/Documents/GitHub/LearningPython/Mod 10 HW.py
#Traceback (most recent call last):
  #File "/Users/amberward/Documents/GitHub/LearningPython/Mod 10 HW.py", line 69, in <module>
    #building = Building()
  #File "/Users/amberward/Documents/GitHub/LearningPython/Mod 10 HW.py", line 56, in __init__
   # super().print_info(b_floor_num=0, t_floor_num=5)
    #^^^^^^^^^^^^^^^^^^
#AttributeError: 'super' object has no attribute 'print_info'

##Process finished with exit code 1##

## the 4th question is posted in mod 9