#kunjesh@charu
# print the value before @, using break statement.
s="kunjesh@charu"

'''for x in s:
    if (x=='@'):
        break
    print(x,end="")'''

# print the value and skip @, using continue statement.
'''for i in s:
    if (i=='@'):
        print("")
        continue
    print(i,end="")'''

# using pass statement.
for i in range(1,11):
    if(i%3==0):
        print(i)
    else:
        pass