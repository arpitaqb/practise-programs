#call function in main program which cal;culate factorial 

def factorial(n):
    if n ==0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
if __name__ ==  "__main__":
    n = int(input("enter number for factorial:"))
    print(factorial(n))