dic = {
    "Name": "Md Nasim Hossen",
    "Age": 23,
    "Salary": 10000,
    "Profession": "Engineer",
    "Sex": "Male"
}

print(dic)

dic.pop("Sex") # pop the sex key and value
print(dic)

dic["Sex"]="Male" #again add Sex
dic.popitem() # pop the last insert or last value
print(dic)


del dic["Age"] # delete the age key
print(dic)

dic.clear() # clear the dic and the length is zero

del dic # completely delete the dictionary
