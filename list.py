# list, append, remove
import random
'''l=[1,2,3]
l.append(4)
l.remove(1)
print(l)'''

l=[]
for i in range(30):
    l.append(random.randint(1,365))
l.sort()
print(l)

i=0
flag=0
while(i<len(l)-1):
    if(l[i]==l[i+1]):
        flag=1
        print("Repeats",l[i],l[i+1])
        #break
        # if you wants only first repeated value then uncomment break statement.
    i=i+1
if (flag==0):
    print("Does not repeat.")
