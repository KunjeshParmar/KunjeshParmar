#fruits=["mango","apple","guava","pineapple","grapes",'orange']
# normal writing
'''newlist=[]
for fruit in fruits:
    if 'n' in fruit:
        newlist.append(fruit.capitalize())
print(newlist)'''


# using list comprehension.
'''newlist=[fruit.capitalize() for fruit in fruits if 'n' in fruit]
print(newlist)'''

# find max in list.
