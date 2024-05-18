r1=[1,2,3]
r2=[2,3,1]
r3=[4,2,1]

s1=[2,3,2]
s2=[2,2,2]
s3=[2,5,1]

a=[]
b=[]
dim=3

a.append(r1)
a.append(r2)
a.append(r3)

b.append(s1)
b.append(s2)
b.append(s3)

print(a)
print(b)

c=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(dim):
    for j in range(dim):
        c[i][j]=a[i][j]+b[i][j]
print(c)