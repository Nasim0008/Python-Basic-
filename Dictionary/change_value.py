dic = {
    "Name": "Md Nasim Hossen",
    "Age": 23,
    "Salary": 10000,
    "Profession": "Engineer"
}

print(dic)

dic["Profession"]="Software Engineer"

print(dic)
# we can change the key with update function
dic.update({"Salary": 2000000})
print(dic)
