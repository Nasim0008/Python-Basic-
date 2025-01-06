# symmetric difference keeps the value that are not present in both

s1 = {1,2,3,4,"Nasim"}
s2 = {1,2,3,4}
s1.symmetric_difference_update(s2) # find the symmetric_difference without extra set
print(s1)