'''year=int(input("Enter the year: "))

while(year!=1947):
    print("You entered wrong year, Please try again.")
    year = int(input("Enter the year: "))
print("Congratulations! You are correct this time.")'''

#Find the factorial of a number.

'''num=int(input("Enter the number: "))
fact=1
if(num<0):
    print("Not define.")
else:
    while(num>0):
        fact=fact*num
        num=num-1
    print(fact)'''

# find the numer of digit.
'''num=abs(int(input("Enter a number: ")))
digit=1
while(num>9):
    num=num//10
    digit=digit+1
print(digit)'''

#1. reverse the number.
'''num=int(input("Enter a number: "))
absnum=abs(num)
if(num>=0):
    rev = num % 10
    num = num // 10
    while (num > 0):
        r = num % 10
        num = num // 10
        rev = rev * 10 + r
    print(rev)
else:
    rev=absnum%10
    absnum=absnum//10
    while(absnum>0):
        r=absnum%10
        absnum=absnum//10
        rev=rev*10+r
    print(rev-rev*2)'''

#2. reverse the number.
'''num=int(input("Enter a number: "))
absNum=abs(num)
rev=absNum%10
absNum=absNum//10

while(absNum>0):
    r=absNum%10
    absNum=absNum//10
    rev=rev*10+r
if(num>0):
    print(rev)
else:
    print(rev-rev*2)'''

# find number is palindrome or not.
num=int(input("Enter a number: "))
absnum=abs(num)
rev=absnum%10
absnum=absnum//10

while(absnum>0):
    r=absnum%10
    absnum=absnum//10
    rev=rev*10+r
if(num<0):
    rev=(rev-rev*2)
if(num==rev):
    print("Palindrome")
else:
    print("Not a palindrome")


