# 1)Print Numbers from 1 to N

N = int(input())
for i in range(1,N+1):
    print(i,end =" ")

# 2)Print Even Numbers up to N

N = int(input())
for i in range(2, N + 1, 2):
    print(i, end=" ")

# 3)Sum of First N Natural Numbers

N = int(input())
sum = 0 
for i in range(1,N+1):
    sum += i
print(sum)

# 4)Multiplication Table
n = int(input())
for i in range(1,11):
    print(n,"*",i,"=",n*i)

# 5)Factorial of a Number

N = int(input())
fact = 1
for i in range(1,N+1):
    fact *= i
print(fact)

# 6)Count Digits in a NUmber

N = int(input())
if N == 0:
    print(1)
else:
    count = 0
    while N > 0:
        N //= 10
        count += 1
    print(count)

# 7)Reverse a Number

N = int(input())
reverse = 0
while N > 0:
    digit = N % 10
    reverse = reverse * 10 + digit
    N //= 10
print(reverse)

# 8) Sum of Digits

N = int(input())
digit_sum = 0
while N > 0 :
    digit = N % 10
    digit_sum += digit
    N //= 10
print(digit_sum)

# 9)Print Squares from 1 to N

N = int(input())
for i in range(1,N+1):
    print(i*i,end=" ")

# 10)Print Odd Numbers in a Range

A,B = map(int,input().split())
for i in range(A,B+1):
    if i%2 != 0:
        print(i,end=' ')

# 11)Number Divisors

N = int(input())
for i in range(1,N+1):
    if N % i == 0:
        print(i,end = ' ')

# 12)Check Prime Number

N = int(input())
is_prime = True
if N == 1:
    is_prime = False
else:
    for i in range(2, N):
        if N % i == 0:
            is_prime = False
            break
if is_prime:
    print("Prime")
else:
    print("Not Prime")

# 15)Calculate Power


