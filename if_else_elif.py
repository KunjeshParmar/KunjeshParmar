#1. to find number is odd or even.

'''num=int(input("Enter the number: "))

if (num%2==0):
    print("Even")
else:
    print("Odd")'''

#2. to find the grade of student marks.
# a= >=90, b= >=80, c= >=70, d= >=60, fail= <60.

marks=int(input("Enter the marks: "))

if(marks>=0 and marks<=100):
    if(marks>=90):
        print("A")
    elif(marks>=80):
        print("B")
    elif(marks>=70):
        print("C")
    elif(marks>=60):
        print("D")
    else:
        print("Fail")
else:
    print("Invalid")

