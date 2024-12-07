"""
capitalize() function only works with the s[0]
if the s[0] is lower case character then it converte to the upper case
if the s[0] is not lower case character, then it remains same. applied for the number or special character
"""

s = "md nasim hossen"
s.capitalize() # No change (md nasim hossen)
s1 = s.capitalize() # Md nasim hossen
print(s1)

a = "10 is my favourite number"
a1 = a.capitalize() # 10 is my favourite number (No change)
print(a1)