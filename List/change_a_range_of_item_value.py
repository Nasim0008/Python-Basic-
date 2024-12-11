# when number of inserting element and number of replacing index is equal:
li = ["A","X","Y","D","E"]
li[1:3]=["B","C"]

"""
Here, Replacing index: 1,2
And, Inserting element: B,C
both of them are equal.
so here changing process will be
li[1] = "B"
li[2] = "C"
"""
print(li)



# when number of inserting element is more than number of replacing index:
'''If you insert more items than you replace, the new items will be inserted,
where you specified, and the remaining items will move accordingly'''

li = ["A","X","Y","E","F"]
n1 = len(li)
print(n1)
li[1:3]=["B","C","D"]
n2 = len(li)
print(n2) # size will be increase

"""
Here, Replacing index: 1,2
And, Inserting element: B,C,D
Inserting element is more than replacing index
so here changing process will be
li[1] = "B"
li[2] = "C"
li[3] = "D"
"""
print(li)



# when number of inserting element is less than number of replacing index:
'''If you insert less items than you replace, the new items will be inserted,
where you specified, and the remaining items will move accordingly'''

li = ["A","X","Y","C","D"]
n1 = len(li)
print(n1)
li[1:3]=["B"]
n2 = len(li)
print(n2) # size will be decrease

"""
Here, Replacing index: 1,2
And, Inserting element: B
Inserting element is less than replacing index
so here changing process will be
li[1] = "B"
"""
print(li)

