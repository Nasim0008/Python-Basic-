
"""
variable create an outside of a function is called global variable
Global variables can be used by everyone, both inside of functions and outside.
"""

x = "Md Nasim Hossen"


def myname():
    x = "Bangladesh" # use same variable as global variable
    print(x)


myname() # output: Bangladesh , inside the function we can change it
print(x) # output : Md Nasim Hossen, an outside of the function we can not change it