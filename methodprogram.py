#string methods 
s = "Arpita"
print(s.capitalize())
print(s.casefold())
print(s.center(40))
print(s.endswith("a"))
print(s.strip("a"))
print(s.find("a"))
print(s.upper())
print(s.lower())

#list methods 

l = [ 1, 2, 3, 2, "apple"]

l.append("banana")
print(l)
a = l.copy()
print(a)
print(a.count(2))
l.clear()
print(l)
b = ["cherry", 2,  3]
a.extend(b)
print(a)
print(a.index(2))
a.insert(3, "mango")
print(a)
a.pop()
print(a)
a.pop(3)
print(a)
a.remove(2)
print(a)
a.reverse()
print(a)
c = [1,5,2,8,0,3]
c.sort()
print(c)

#dictionary methods

d = {1: "apple", "a": "aaa", 2: "banana"}
print(d)
z = d.copy()
print(z)

# d.clear()
print(d)
x= ("1", "2", "3", 4)
y = 0
n= dict.fromkeys(x,y)
print(n)
m = dict.fromkeys(x)
print(m)

print(z.get(1))
print(z.get("a"))
print(z.items())
print(z.keys())
d.pop(1)
print(d)
d.popitem()
print(d)
d.setdefault("ab", "cde")
d.setdefault("ef")
print(d)
d.update({"ab": "cde"})
print(d)
print(d.values())

#tuple methods
t = (1,2,4,7,2,"apple", 2,54, 5, 2)
print(t.count(2))
print(t.index(4))
print(t.index("apple"))
print(t.count(1000))

#set methods
s = {1,4,3,7,3}
print(s)
s.add(5)
print(s)
a = s.copy()
# s.clear()
print(s)
print(a)
z = a.difference(s)
print(z)