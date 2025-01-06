# symmetric difference keeps the value that are not present in both

s1={1,2,3,4,5,6,"Nasim"}
s2={"a","b","c","d","Nasim"}

s= s1.symmetric_difference(s2) # {1,2,3,4,5}
print(s)

# we also can use ^ operator for symmetric_difference  method
s3 = s1 ^ s2
print(s3)



