# union means join two or multiples set

s1 = {1,3,4,5,6}
s2 = {"a","b","c","d"}
s3={False,True,False}
s4={"A","B","C"}
s1=s1.union(s2,s3,s4) # s1+s2+s3+s4
print(s1)


# we can | instead of union() function
s1 = {1,3,4,5,6}
s2 = {"a","b","c","d"}
s3={False,True,False}
s4={"A","B","C"}
s1=s1|s2|s3|s4
print(s1) #s1+s2+s3+s4
