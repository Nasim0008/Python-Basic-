"""
By using global keyword, we can de clear global variable inside the function
"""

def myname():
    global x
    x = "Md Nasim"
    print(x)


myname()

print("My name is " , x)