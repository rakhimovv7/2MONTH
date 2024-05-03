#1:
class MagicCalculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def __add__(self, other):
        return self.number1 + other
    
    def __sub__(self, other):
        return self.number1 - other
    
    def __mul__(self, other):
        return self.number1 * other
    
    def __truediv__(self, other):
        return self.number1 / other
    
    def __floordiv__(self, other):
        return self.number1 // other


result = MagicCalculator(15, 5)

print(result + 10)
print(result - 5)
print(result * 3)
print(result / 4)
print(result // 3)

# Доп. задание :

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f"название книги - {self.title}, автор - {self.author}, год издания - {self.year}"
    
    def __lt__(self, other):
        return self.year < other.year
    def __gt__(self, other):
        return self.year > other.year   
    def __eq__(self, other):
        return self.year == other.year
    def __ne__(self, other):
        return self.year != other.year
    def __ge__(self, other):
        return self.year >= other.year
    def __le__(self, other):
        return self.year <= other.year
    
book1 = Book("Война и мир", "Лев Толстой", 1869)    
book2 = Book("Шум и ярость", "Уильям Флонкер", 1929) 
book3 = Book("Человек-неведимка", "Ральф Эллисон", 1952)   

print(book1)
print(book2)
print(book3)

print(book1 < book2, book2 < book3, book3 < book1)
print(book1 > book2, book2 > book3, book3 > book1)
print(book1 > book2, book2 > book3, book3 > book1)
print(book1 > book2, book2 > book3, book3 > book1)
print(book1 != book2, book2 != book3, book3 != book1)
print(book1 >= book2, book2 >= book3, book3 >= book1)
print(book1 <= book2, book2 <= book3, book3 <= book1)


    




   