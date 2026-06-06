# 1)Solid Square Star Pattern

n =int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end =' ')
    print()

# 2) Hollow Square

n= int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == 0 or j == 1 or j == 0:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 3)Hollow Square with X

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n or i == j or i + j == n+1:
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()

# 4)Right angle triangle

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i >= j:
            print("*",end = " ")
        else:
            print(" ", end = " ")
    print()

# 5)Inverted Right Triangle

n = int(input())
for i in range(1,n+1):
    for j in range(1, n+1):
        if i+j <= n+1:
            print("*",end =" ")
        else:
            print(" ",end = " ")
    print()

# 6)Left anlge triangle

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i <= j :
            print("*",end = " ")
        else:
            # Remove space to grt reverse pyrarid
            print(" ",end=" ")
    print()

# 7) Diamond

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j >= n:
            print("*",end = " ")
        else:
            # Remove space to grt reverse pyrarid
            print("",end=" ")
    print()

for i in range(2,n+1):
    for j in range(1,n+1):
        if i <= j :
            print("*",end = " ")
        else:
            # Remove space to grt reverse pyrarid
            print("",end=" ")
    print()


# 8)Hourglass Star Pattern / X Triangle Pattern

n = int(input())
for i in range(1, n+1):
    for j in range(1,n+1):
        if i <= j:
            print("*",end = " ")
        else:
            print("",end= ' ')
    print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j >= n:
            print("*",end = ' ')
        else:
            print("",end = " ")
    print()

# 9) Full Pyramid Star Pattern

n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(2*i+1):
        print("*",end =" ")
    print()


# 10)Inverted Full Pyramid Star Pattern

n =int(input())
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end =" ")
    for j in range(2*i+1):
        print("*" , end = " ")
    print()


# 11)Hollow Pyramid Star Pattern

n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end = "")
    for j in range(2*i-1):
        if i == n or j == 2*i-2 or j == 0:
            print("*",end = "")
        else:
            print(" ",end = "")
    print()

# 12)Number Triangle Pattern

n =int(input())
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j,end=" ")
    print()




