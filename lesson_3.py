# class laptops:
#     def __init__(self, model, os, memory):
#         self.model = model
#         self._os = os
#         self._memory = memory
        
# huawey = laptops("Huawei", "Windows 11", 512)        
# print(huawey.model)
# print(huawey._os)
# print(huawey._memory)

class Father:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def work(self):
        print("Работа")


class Mother:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def cook(self):
        print("Готовка")


class Child(Father, Mother):
    def cook(self):
        print("Я не умею готовить")

david = Child("David:", 15)
david.work()
print(david.name)
david.cook()


                