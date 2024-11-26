# python docstring:

"""
python docstring is a string literal with Triple quote which is use right after the function
it is written bellow the function, class, modules for describing what the function do.
"""

def addition(a,b):
    "Finding the summation of a and b"
    return a+b

# print the docstring of addition function
print(addition.__doc__)  # output: Finding the summation of a and b