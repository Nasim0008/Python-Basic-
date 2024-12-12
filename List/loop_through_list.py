li = ["one","two","three","four","five","six"]

# print all the item using for loop (item based)
for value in li:
    print(value,end=" ")

print(end="\n") # for new line

# print all the item using for loop (index based)
for i in range(len(li)):
    print(li[i],end=" ")

print(end="\n")

# print all the item using while loop (index based)

i =0
while i<len(li):
    print(li[i],end=" ")
    i+=1