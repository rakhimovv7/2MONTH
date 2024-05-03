class GeeksPeople:
    def __init__(self,name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"имя = {self.name}, email - {self.email}, номер - {self.phone}"
    
class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study):
        GeeksPeople.__init__(self,name, email, phone)
        self.student_id = student_id
        self.group_wehre_study = group_where_study

    def study(self):
        return f"{self.name} учится в группе - {self.group_wehre_study}"


class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach):
        GeeksPeople.__init__(self,name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def teach(self):
        return f"{self.name} преподает группе - {self.group_where_teach}"


class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        super().__init__(name, email, phone)
        self.admin_id = admin_id
        
    def creaty_group (self,group):
        return f"{self.name} открыл новую группу - {group}"
    
class Mentor(Student, Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study,teacher_id, group_where_teach):
        super().__init__(name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone,teacher_id, group_where_teach)

    def mentor(self):
        print(f"{self.name} помогает группе - {self.group_where_teach}")

people = GeeksPeople("Хожиакбар","takhirow77@gmail.com", +996990530084,)
student1 = Student("Абдуллох", "rahimowvv@gmail.com", +996552847773, 845656, "17-1B" )
teacher1 = Teacher("Сыймык", "abdykadyrov_s@gmail.com", +996555555555, 4628456, "17-1B")
admin1 = Admin("Нурболот", "nurbolot@gmail.com", +996555555555, 464585656)
mentor1 = Mentor("Кудбухон", "kudbuhon@gmail.com", +996554444444, 462584, "15-2B", 462584, "13-1D")


mentor1.mentor()
print(mentor1.study())
print(mentor1.teach())
print(people)
print(student1.study())
print(teacher1.teach())
print(admin1.creaty_group("18-1A"))
