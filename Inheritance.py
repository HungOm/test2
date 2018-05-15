class SchoolMember:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    def tell (self):
        print("Name : {} and Age: {}".format(self.name,self.age))

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print("salary:",self.salary)

class Student(SchoolMember):

    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
    def tell(self):
        SchoolMember.tell(self)
        print("Marks:", self.marks)

t= Teacher('Amos',22,3000)
s=Student("MoninJ",15,85)

print()

members = [t,s]

for member in members:
    member.tell()
