
"""
variable create an outside of a function is called global variable
Global variables can be used by everyone, both inside of functions and outside.
"""

x = "Md Nasim Hossen"


def myname():
    print(x)


myname()