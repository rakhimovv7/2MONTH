class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @property
    def memory(self):
        return self.__memory

    def __make_computations(self, operator):
        if operator == '+':
            result = self.__cpu + self.__memory
        elif operator == '-':
            result = self.__cpu - self.__memory
        elif operator == '*':
            result = self.__cpu * self.__memory
        elif operator == '/':
            if self.__memory != 0:
                result = self.__cpu / self.__memory
            else:
                result = "Ошибка!!! Вы вели не верный формат"
        else:
            result = "Ошибка!!! Вы вели не верный формат"
        return result

    def users(self, operator):
        result = self.__make_computations(operator)
        print(f"Результат {self.__cpu} {operator} {self.__memory} равен = {result}")

computer = Computer(4, 2)
computer.users('+')   
computer.users('-')   
computer.users('*') 
computer.users('/')  

class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    @property
    def memory_card(self):
        return self.__memory_card
    
    def info(self):
        print(f"CPU ноутбука = {self.cpu}, память ноутбука - {self.memory} гб,  карта памяти ноутбука - {self.memory_card} гб ")

res1 = Laptop( "i3-7100U", 4, 8 )
res2 = Computer(4, 8)
res1.info()
res2.users("+")
res2.users("-")
res2.users("*")
res2.users("%")

print(res1.cpu, res1.memory, res1.memory_card)
print(res2.cpu, res2.memory, computer.cpu, computer.memory)
