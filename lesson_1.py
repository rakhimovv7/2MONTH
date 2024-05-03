class Car:
    wheels = 4
    def __init__(self, model, color ):
        self.model = model
        self.color= color       

    def info(self):
            print(f"Model - {self.model}, color - {self.color} ")
       

super_car = Car("Mersedes - cls", "black")
super_car_2 = Car("BMW - m5", "white")
# print(super_car.wheels)
# print(super_car.wheels)
# print(super_car.model)
# print(super_car_2.model)
# super_car.info()
super_car_2.info()