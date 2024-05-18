import random
l=[]
# searching the value using for loop.
'''for i in range(30):
    l.append(random.randint(1,100))
l.sort()
print(l)
n=int(input("Enter a number: "))

flag=0
for k in range(len(l)):
    if (n==l[k]):
        print("Found")
        flag=1
if (flag==0):
    print("Not found")'''

# searching the value using while loop.

for i in range(30):
    l.append(random.randint(1,50))
l.sort()
print(l)

n=0
while(n>-1):
    n = int(input("Enter a number, enter -1 to exit: "))
    flag = 0
    for j in range(len(l)):
        if (n==l[j]):
            print("Found")
            flag=1
            break
    if (flag==0):
        print("Not found")
