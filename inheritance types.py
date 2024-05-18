# 1. Simple or Single inheritance. Single inheritance enables a derived (Child) class to inherit
# properties from a single parent class.

'''class Parent():
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name, self.age)

class Child(Parent):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        self.city=city

    def display(self):
        super().display()
        print(self.city)

obj=Child("Kunjesh",28, "Noida")
obj.display()'''

#2. hierarchical inheritance- When more than one derived (Child) class are created from a single parent class
# this type of inheritance is called hierarchical inheritance.

'''class Parent():
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name, self.age)

class Employe1(Parent):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department=department

    def display(self):
        super().display()
        print(self.department)


class Employe2(Parent):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        super().display()
        print(self.salary)

obj1=Employe1("Aman",35,"IT")
obj1.display()
obj2=Employe2("Suman",30, 65000)
obj2.display()'''


#3. Multilevel- In multilevel inheritance, features of the base (Parent) class and the derived (Child) class
# are further inherited into the new derived class (Lower child).

'''class Parent():
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name, self.age)

class Child(Parent):
    def __init__(self,name, age, clgName):
        super().__init__(name, age)
        self.clgName=clgName

    def display(self):
        super().display()
        print(self.clgName)

class Gchild(Child):
    def __init__(self, name, age, clgName, trade):
        super().__init__(name, age, clgName)
        self.trade=trade

    def display(self):
        super().display()
        print(self.trade)

obj1=Gchild("Ramita",26,"IITM",'Bsc')
obj1.display()'''

# 4. Multiple Inheritance- When a class can be derived from more than one base class
# this type of inheritance is called multiple inheritances.

class Parent1():
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name, self.age)

class Parent2():
    def __init__(self, city):
        self.city=city

    def display(self):
        print(self.city)

class Child(Parent1, Parent2):
    def __init__(self, name, age, city):
        super().__init__(name,age,city)

    def display(self):
        super().display()

obj=Child("Chotu",25,"Delhi")
obj.display()


