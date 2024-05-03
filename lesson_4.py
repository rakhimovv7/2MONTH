class ElektroCar:
    def __init__(self, power, battery):
        self.power = power
        self.battery = battery

    def info(self):
        print(f"Мощность - {self.power} Vat, \nЗаряд батареи - {self.battery} Mac")

    def __repr__(self):
        return f"Мощность - {self.power} Vat, \nЗаряд батареи - {self.battery} Mac"

car = ElektroCar(120, 20000)
car.info()
print(car)