import random
l=[]
for i in range(10):
    l.append(random.randint(1,6))
print(l)

x=[]
while(len(l)>0):
    min=l[0]
    for j in range(len(l)):
        if (l[j]<min):
            min=l[j]
    x.append(min)
    l.remove(min)

print(x)