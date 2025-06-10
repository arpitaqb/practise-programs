n = 5
# for i in range(n +1):
#     for j in range(i,n+1):
#         print("*", end=" ")
#     print()

# for i in range(0,n):
#     for j in range(i, n+1):
#         print("*", end=" ")
#     print()

# for i in range(1, n+1):
#     print("*" * i)

# for i in range(n, 0, -1):
#     print("*" * i)


# for i in range(1, n+1):
#     for j in range(i):
#         print("O", end=" ")
#     print()

    
for i in range(n):
    for j in range(n, i, -1):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")