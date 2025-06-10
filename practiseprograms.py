#1. check for number 

num = int(input("enter a number:"))

if num >= 0:
    if num ==0:
        print("zero")
    else:
        print("positive")
else:
    print("negative")


#2. check if given number is even or odd

a = int(input("enter number:"))
if a%2 == 0:
    print("given number is even")
else:
    print("given number is odd")

#3. sum of n natural number

n = int(input("enter n number for sum:"))
sum = 0 
for i in range(0,n+1):
    sum += i
print(sum)
 
s = (n*(n+1))/2 # by formula
print(s)

#4. sum of number into givemn range
a1 = int(input("1st number:"))
a2 = int(input("2nd number:"))
s1 = 0
for i in range(a1, a2+1):
    s1 += i
print(s1)


#5. find the grater number into 3 numbers
n1 = int(input("1st number"))
n2 = int(input("2st number"))
n3 = int(input("3st number"))

if n1>n2 and n1>n3:
    print(f"{n1} is greatest number")
elif n2>n1 and n2>n3:
    print(f"{n2} is greatest number")
else:
    print(f"{n3} is greatest number")

#6. check for prime number 
n = int(input("enter number:"))
for i in range(2, int((n/2)+1)):
    if n%i == 0:
        print("not prime")
        break
    else:
        print("prime")
        break 
        
#7. sum of digits of number
a = input("number:")
sum = 0
for i in a:
    sum = sum + int(i)
print(sum) 

#8.reverse a number
n = int(input("enter number:"))
temp = n 
rev = 0
while n>0:
    rem = n%10
    rev = (rev * 10)+rem
    n = n //10

print(rev)

#9. palindrom number
n = int(input("enter number:"))
temp = n
rev = 0 
while n>0:
    rem = n%10
    rev = (rev *10) + rem
    n = n//10

if rev == temp:
    print("palindrom")
else:
    print("not palindrom")

#10. armstrong number 
n = input("enter number:")
l = len(str(n))
s = 0 
for i in n:
    s += int(i) ** l

if s == int(n):
    print("armstrong")
else:
    print("not armstrong")

#11. fibonaci series
f1 = 0 
f2 = 1 
n = int(input("number "))

for i in range(n+1):
    f3 = f1+f2
    print(f3)
    f1 = f2
    f2 = f3 

#11. factorial 

def fun(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fun(n-1)
    
n = int(input("enter number:"))
print(fun(n)) 

#12. factor of the number 

n = int(input("enter number:"))
i = 1
while i <= n:
    if n % i == 0:
        print(i, end=" ")
    i += 1
    