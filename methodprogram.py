"""
s = "Arpita"
print(s.capitalize())
print(s.casefold())
print(s.center(40))
print(s.endswith("a"))
print(s.strip("a"))
print(s.find("a"))
print(s.upper())
print(s.lower())
"""
#list methods 

l = [ 1, 2, 3, 2, "apple"]

l.append("banana")
print(l)
a = l.copy()
print(a)
print(a.count(2))
l.clear()
print(l)
b = "cherry"
a.extend(b)
print(a)