#1
class Person:

    def __init__ (self, fullname, age, is_married):
        self.fulname = fullname
        self.age = age
        self.is_married = is_married
#2
    def introduce_myself(self):
        print(f"Меня зовут - {self.fulname}, мне - {self.age}, и я - {self.is_married}")

result = Person("Рахимов Абдуллох", 17,  "не женат")
result2 = Person("Тахиров Хожиакбар", 17,  "не женат")

result.introduce_myself()
result2.introduce_myself()



#Доп задание:

#1:
class Teacher (Person):
    def __init__(self, fullname, age, is_married, exprience):
        super().__init__(fullname, age, is_married)
        self.exprience =  exprience
        self.salary = 0
#2
    def work(self):
        for users in range(self.exprience):
            self.salary+=3000
        print(f"Ваша зарплата состовляет - {self.salary}")

#3
    def introduce_myself(self):
        print(f"Привет, меня зовут - {self.fulname}, мне {self.age} лет, я {self.is_married} и мой стаж работы - {self.exprience} - года")

users = Teacher("Сыймык", 19, "не женат", 3)
users.introduce_myself()
users.work()
