# intersection keeps only the duplicate value from both of the set

s1={1,2,3,4,5,6,"Nasim"}
s2={"a","b","c","d","Nasim"}

s= s1.intersection(s2) # keeps only duplicate or present in both set
print(s)

# we also can use & operator for intersection method
s3 = s1&s2
print(s3)

# for multiple set
s4={2,34,4,5,"Nasim"}

s5 = s1.intersection(s2,s4)
print(s5)

s6 = s1 & s3 & s4

# Intersection set (False = 0) and (True =1) same value