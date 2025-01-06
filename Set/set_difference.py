# set difference keeps the value from the first set that are not present in the second set

s1={1,2,3,4,5,6,"Nasim"}
s2={"a","b","c","d","Nasim"}

s= s1.difference(s2) # {1,2,3,4,5}
print(s)

# we also can use & operator for intersection method
s3 = s1-s2
print(s3)

# for multiple set
s4={2,34,4,5,"Nasim"}

s5 = s1.difference(s2,s4) #{1,3,6}
print(s5)

s6 = s1 - s3 - s4
print(s6)

