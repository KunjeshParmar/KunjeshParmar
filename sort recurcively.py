# sort obvious way.
l=[5,9,8,6,10,85,109,2]

def minimum(l):
    mini=l[0]
    for i in range(len(l)):
        if (l[i]<mini):
            mini=l[i]
    return mini
#print(minimum(l))

def sort(l):
    if (l==[]) or (len(l)==1):
        return l
    m=minimum(l)
    l.remove(m)
    return [m]+ sort(l)
print(sort(l))
