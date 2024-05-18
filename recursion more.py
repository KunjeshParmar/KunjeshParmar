# Adding n numbers.
'''def add(n):
    if n==1:
        return n
    else:
        return add((n-1))+n
n=100
print(add(n))'''

# Factorial of n numbers.
'''def fact(n):
    if n==1:
        return 1
    else:
        return (fact(n-1))*n
print(fact(5))'''

# find 5 in list.

def find(l):
    if (len(l)==0):
        return 0
    if (l[0]==5):
        return 1
    else:
        find(l[1:len(l)])
ans= (find([1,9,7,3,5,4,9]))
print(ans)
