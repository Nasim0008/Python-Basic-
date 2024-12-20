# set items are unordered, unchangeable, and allow duplicate value


# Unordered:
"""
unordered means the items in a set does not have any define order.
set item can appear in different order every time, we can not redefine in different ordered.
"""

# Unchangeable:
"""
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.
"""

# Duplicate not allowed:
"""
Sets cannot have two items with the same value.
"""

se = {1,2,3,3,3,3,4,5,56,1}
print(se)

#The values True and 1 are considered the same value in sets, and are treated as duplicates:
se = {1,1,2,3,4,"one","two","one",True,1,True}
print(se)

#The values False and 0 are considered the same value in sets, and are treated as duplicates:
se = {1,0,False,False,0}
print(se)
