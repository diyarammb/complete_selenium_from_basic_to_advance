class Person():
    def greet(self):
        print("I am  Person")

class Teacher(Person):
    def greet(self):
        print("I am Teacher")

class student(Person):
    def greet(self):
        print("I am Students")

class Assign(Teacher,student):
    def greet(self):
        print("Teaching assistent")
a=Assign()
# a.greet()
# MRO
# help(Assign)
print(Assign.__mro__)


