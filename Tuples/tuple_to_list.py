"""
tuple are unchangeable, we can not add, delete, insert, modify of the tuple
so , we can convert the tuple to the list then after the update we can again can convert the tuple
"""

tp = (1,2,3,4,5,6)
li = list(tp) # tuple to the list
# we can modify the list as wish we can
tp = tuple(li) # tuple to the list
print(tp)