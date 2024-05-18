class Student():
    def __init__(self, rollnb,name,total):
        self.rollnb=rollnb
        self.name=name
        self.total=total

    def display(self):
        print(self.rollnb, self.name, self.total)

    def result(self):
        if self.total>200:
            print("Pass")
        else:
            print("Fail")

s0=Student(0,"Kunjesh",500)
s0.display()
s0.result()

s1=Student(1,"Munna",168)
s1.display()
s1.result()