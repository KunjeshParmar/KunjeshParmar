# child class (Student and Employee inherit the properties of parent class (Person))
class Person():
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name, self.age)

class Student(Person):

    def __init__(self,name, age, marks):
        super().__init__(name, age)
        self.marks=marks

    def display(self):
        super().display()
        print(self.marks)

s1=Student("Kunjesh",28, 500)
s1.display()

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary=salary

    def display(self):
        #super().display()
        # here using method overloading.
        print(self.name, self.age, self.salary)

emp=Employee("Charu", 26, 80000)
emp.display()