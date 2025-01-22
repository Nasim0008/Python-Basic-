dic = {
    "Name": "Md Nasim Hossen",
    "Profession": "Software Engineer",
     "Age": 22,
     "Marital Status": False
}

# print the keys one by one
for x in dic: # without function
    print(x)

for x in dic.keys(): # with function
    print(x)

#print the value one by one
for x in dic: # without function
    print(dic[x])

for x in dic.values(): #with function
    print(x)


# print key and values both
for x in dic: #without function
    print(x, dic[x])


for x,y in dic.items(): #with function
    print(x,y)

