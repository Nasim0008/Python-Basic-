# union() function allow you to join with the set and others container like list,tuples

se = {1,2,3,4,5}
tu = ("a","b","c")
tu2=("one","tow","three")
li1=["A","B","C"]
li2=["Bangla","English","Math"]
s1= se.union(tu) # set with single tuple
s2 = se.union(tu,tu2) # set with multiple tuple
s3=se.union(li1)
s4 = se.union(li1,li2,tu) # set with list and tuples
print(s1)
print(s2)
print(s3)
print(s4)

# we can not use | operator for joining the set

