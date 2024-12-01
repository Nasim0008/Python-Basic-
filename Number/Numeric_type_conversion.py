a = 10 #int
b = float(a) # convert int to float
c = complex(a) # convert int to complex
print(a,b,c)

a = 100.100 #float
b = int(a) # convert float to int
c = complex(a) # convert float to complex
print(a,b,c)

a = 4+5j # complex number can not convert to the int,float
print(a)