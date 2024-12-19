tp = (10,20,30,40,50,60,70,80,90,100)

print(tp)

# if the number of variable is less than the number of value , then we can use asterisk(*) to assign the value rest of the value
(a,b,*c) = tp

print(a)
print(b)
print(c)


(c,*d,p)=tp
print(c)
print(d)
print(p)