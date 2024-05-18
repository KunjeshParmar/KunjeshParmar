# find min in list
'''def list_min(l):
    mini=l[0]
    for i in range(len(l)):
        if (l[i]<mini):
            mini=l[i]
    return mini

l=[25,15,8,6,9]
print(list_min(l))'''

# sort list

def sort(l):
    x = []
    while (len(l) > 0):
        mini=l[0]
        for i in range(len(l)):
            if (l[i]<mini):
                mini=l[i]
            #return mini
        x.append(mini)
        l.remove(mini)
    return x

l=[8,9,6,5,1,3,10]
print(sort(l))

