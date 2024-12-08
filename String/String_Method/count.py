"""
we can count the particular character or a particular sequence of character by using this count function
"""
s = "My name is Md Nasim Hossen. I love my name very much"

cnt = s.count("I") # count particular character (from 1st to the last of the string)
print(cnt)

cnt = s.count("name") # count a particular sequence of character (from 1st to the last of the string)
print(cnt)

cnt = s.count("name",20,100) # count from 20th index to the 99th index
print(cnt)



