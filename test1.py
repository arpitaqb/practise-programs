#basic calculator that perform basic operations.

print("welcome to basic calculation")

a = int(input("enter first number:"))
b = int(input("enter second number:"))
print("for addition enter +")
print("for substraction enter -")
print("for multiplication enter *")
print("for division enter /")

c =input("enter your choice:")

if c == '+':
    print("the addition of given number is: ", a+b)
elif c == '-':
    print("the substraction of given number is:", a-b)
elif c == '*':
    print("the multiplication of given number is:", a*b)
elif c == '/':
    print("the division of given number is ", a/b)
else:
    print("enter valid choice")

