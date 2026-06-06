
# 6)

n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print("*",end = " ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end = " ")
    print()

# 17) 

n = int(input())
for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print("*" , end="")
        else:
            print(" ",end="")
    print()

# 18)

n =int(input())
mid = n//2
for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 22) 

n = int(input())
for i in range(n):
    if i % 2 == 1:
        print(" ",end="")
    for j in range(n):
        print("*",end=" ")
    print()

# 19)

n = int(input())
for i in range(n):
    spaces = 2*i
    stars = 2*(n-i) - 1
    print(" " * spaces + "* " * stars)
for i in range(n - 2, -1, -1):
    spaces = 2 * i
    stars = 2 * (n-i) -1
    print(" " * spaces + "* " * stars)


# 24)

n = int(input())
for i in range(1,n+1):
    print(" " * (n - i),end="")
    for j in range(1, i +1):
        print(j, end =" ")
    print()

# 25)


        
    

    