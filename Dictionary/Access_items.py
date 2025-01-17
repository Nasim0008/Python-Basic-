dic = {
    "Name": "Md Nasim Hossen", #key:value
    "Profession": "Software Engineer", #string
     "age": 22, # int
    "Marital status": False, #bool
    "Salary": 1000000.000, #double
    "Education Qualification": ["SSC","HSC"] # list
}
# print the items
print(dic["age"]) # use square bracket
print(dic.get("age")) # use get function
print(dic["Education Qualification"])
print(dic.get("Educational Qualification"))


#print the keys
key =dic.keys()
print(key)

#print the values
value = dic.values()
print(value)

#print the items
print(dic.items()) 