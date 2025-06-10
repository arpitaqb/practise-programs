#oops concept

#1. inheritence

class parent:
    def __init__(self,name):
        self.name = name 
    
class child(parent):  #this is inheritence
    pass

a = child("arpita")
print(a.name)

#2. polymorphism

class parent1:
    def show(self):
        print("This is parent class")

class child1(parent1):
    def show(self):  #This is method ovverriding
        super().show() #super function is used which call parents class's function
        print("This is child class")

b = child1()
b.show()


#3. abstraction 
from abc import abstractmethod
class parent2:
    @abstractmethod
    def show(self):
        pass

class child2(parent2):
    def show(self):
        print("this is child2")

class child3(parent2):
    def show(self):
        print("this is child 3")

c2 = child2()
c3 = child3()

c2.show()
c3.show()

#4.encapsulation

class parent3:
    def salary(self,name,age, salary):
        self.__salary = salary # private acess modifier (cannot access outside of the class)
        self._age = age # protected acess modifier (cannot access directly)
        self.name = name # public acess modifier (can acess)

    def reveal(self):
        return self.__salary
    
p= parent3()
p.salary("arpita", 20, 50000)
print(p.name)
print(p._age) #by _ we can acess value 
#print(p.age) # this will give an error because it is protected
#print(p.__salary)
print(p.reveal())
