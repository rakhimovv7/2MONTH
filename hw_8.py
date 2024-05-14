import sqlite3
connect = sqlite3.connect("Bank.db")
cursor = connect.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS user(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               surname VARCHAR (100)NOT NULL,
               name VARCHAR (100) NOT NULL,
               age INTEGER NOT NULL,
               email VARCHAR (100) NOT NULL,
               address VARCHAR (100) NOT NULL,
               balance INTEGER NOT NULL DEFAULT 0
               );
               """)

class Bank:
    def register(self):
        self.balance = 0
        self.surname = None
        self.name = None
        self.age = 0
        self.email = None
        self.address = None
     
    def register (self,name, surname, age, email, address):
        self.name = name 
        self.surname = surname
        self.age = age
        self.email = email
        self.address = address
        cursor.execute (f"""INSERT INTO user (name,surname,age,email,address,balance)
                       VALUES('{name}','{surname}','{age}','{email}','{address}',0); """)
        connect.commit()

    def plus_balace(self, amount, youre_name):
        cursor.execute(F"UPDATE user SET balance = balance + {amount} WHERE name = '{youre_name}' ")
        connect.commit()
        self.balance += amount 
    def minus_balance(self, amount, youre_name):
        cursor.execute(F"UPDATE user SET  balance = balance - {amount} WHERE name = '{youre_name}' ")
        connect.commit()
        self.balance -= amount
    def main(self):
        while True:
            print("Выберите команду: ")
            print("1-регистрация 2-Добавление коинов, 3-Отнять коин")
            command = int(input("Введите цифру: "))
            if command ==1:
                name = input("Введите имя человека: ")
                surname = input("Введите фамилию: ")
                age = int(input("Введите возраст: "))
                email = input("введите свой gmail: ")
                address = input("введите свой адрес:")

                self.register(name,surname,age,email,address)

            elif command == 2:
                youre_name = input("Введите имя человека: ")
                if youre_name:
                    amount = int(input("Введите кол-во денег: "))
                else:
                    print("Такого ментора нет")
                self.plus_balace(amount, youre_name)

            elif command == 3:
                youre_name = input("Введите имя человека: ")
                amount = int(input("Введите кол-во денег: "))
                self.minus_balance(amount, youre_name)
            else:
                print("Такой команды нет")

a = Bank()
a.main()