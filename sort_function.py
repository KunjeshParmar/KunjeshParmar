# find mini in list.
def min(l):
    mini=l[0]
    for i in range(len(l)):
        if (l[i]<mini):
            mini=l[i]
    return mini

# sorting function using above function.

def sorting(l):
    x=[]
    while(len(l)>0):
        mini = min(l)
        x.append(mini)
        l.remove(mini)
    return x
l=[85,45,96,25,85,11]
print(sorting(l))
