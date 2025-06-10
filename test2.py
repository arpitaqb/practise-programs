#devlop a number guessing system
import random 

attampt = 5 
a = random.randint(0,20)

while attampt >= 0:
    n = int(input("guess the number:"))
    if n == a:
        print("correct guess, you win!!!!!!!!!")
        break
    elif n > a :
        print("wrong guess, lower the number")
        attampt -= 1
        if attampt == 1:
            print("you have only one last chance")
    else:
        print("wrong guess, attamp for high guess")
        attampt -= 1
        if attampt == 1:
            print("you have only one last chance")