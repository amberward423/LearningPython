class Elevator:
    def __init__(self, b_floor_num=0 , t_floor_num=5):
       self.b_floor_num = b_floor_num
       self.t_floor_num = t_floor_num


    def go_to_floor(self,new_floor,current_floor, end_floor1, end_floor2):
        self.end_floor1= end_floor1
        self.end_floor2= end_floor2
        self.current_floor= current_floor
        self.new_floor= new_floor
        end_floor1 == current_floor + new_floor
        end_floor2 == current_floor - new_floor
        print(input("Enter floor number, please: "))

    def floor_up(self,new_floor,current_floor):
        self.end_floor1 = end_floor1
        self.new_floor = new_floor
        self.current_floor= current_floor
        print(input("Enter floor number, please: "))
        end_floor1= current_floor + new_floor
        print(f"You are now at floor {self.end_floor1}")

    def floor_down(self,new_floor,current_floor, end_floor2):
        self.end_floor2 = end_floor2
        self.current_floor= current_floor
        self.new_floor = new_floor
        print(input("Enter floor number, please: "))
        end_floor2 == current_floor - new_floor
        print(f"You are now at floor {self.end_floor2}")

Elevator.go_to_floor(5,1,5,5, 1)





