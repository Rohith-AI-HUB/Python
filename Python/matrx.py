class Person:
    name = ''
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def displaydata(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

person1 = Person('Mike', 20)
person2  = Person('Joe', 30)
person1.displaydata()
person2.displaydata()