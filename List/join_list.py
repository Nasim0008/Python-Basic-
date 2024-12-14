li1 = [1,2,3,4,5,6]
li2 = ["A","B","C","D","F"]

li3 = li1+li2 # concatenate two list
print(li3)

li4 = li2+li1 # concatenate two list
print(li4)

for x in li2:
    li1.append(x)

print(li1)

li1.extend(li2)
print(li1)