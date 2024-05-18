import string
'''l=list(string.ascii_lowercase)
t=tuple(string.ascii_lowercase)
print(l)

# tuple is fixed in nature. we can not change it.
print(t)'''

t=tuple(string.ascii_lowercase)
s='kunjeshmurarisingh!%^#&&#123bharat'
l=list(s)
new=[]
print(l)
for i in l:
    if i in t:
        new.append(i)
print(new)
