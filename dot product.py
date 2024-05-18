x=[1,2,3,4]
y=[4,5,6,7]
# dot_product= 1*4 + 2*5 + 3*6  + 4*7

sum=0
for i in range(len(x)):
    sum=sum+ x[i]*y[i]
print(sum)
