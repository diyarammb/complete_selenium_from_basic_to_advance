# class MyClass():
#     a=10
#     def __init__(self,x):
#         self.x=x
#     def method1(self):
#         print(self.x)
#
#     @classmethod
#     def method2(cls):
#         print(cls.a)
#
# MyClass.method2()
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"I am  {self.name}  , {self.age} Years Old")
    @classmethod
    def from_str(cls,s):
        name,age =s.split(',')
        return cls(name,int(age))
    @classmethody
    def from_dic(cls,d):
        return cls(d['name'],d['age'])


s="Daya , 23"
p=Person.from_str(s)
p.display()

print("=================================")
d={"name":"Awais","age":21}
p=Person.from_dic(d)
p.display()

