#inheritance
#simple inheritance
#hierarchial inheritance
#multiple inheritance
#multilevel inheritance
#from "file" import "class"
class Parent1:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display1(self):
        print(self.name,self.age)

class Parent2:
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight
    
    def display2(self):
        print(self.height,self.weight)

class Child1(Parent1,Parent2):
    def __init__(self,name,age,marks,height,weight):
        super().__init__(name,age)
        super().__init__(height,weight)
        self.marks = marks

    def display(self):
        super().display1()
        super().display2()
        print(self.marks)

class Child2(Parent1,Parent2):
    def __init__(self,name,age,salary,height,weight):
        super().__init__(name,age)
        super().__init__(height,weight)
        self.salary = salary

    def display(self):
        super().display1()
        super().display2()
        print(self.salary)

c1 = Child1('Jill',18,99,160,72)
c1.display()

c2 = Child2('Jack',25,1800000,180,84)
c2.display()