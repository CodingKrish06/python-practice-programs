# vo and con

ch = input("Enter the chara")
ch = ch.upper()
if ch >= 'A' and ch <= 'Z':

    if ch in "AEIOUaeiou":
        print("v")
    else:
        print("C")
else:
    print("Not an Alphatent")



ch = input()
if ch.isalpha():
    print("It is an Alphabet")
elif ch.isdigit():
    print("It is an Digit")
else:
    print("It is a Special Symbol")

#Check Single Digit, Double Digit or Three Digit Number

num = int(input("Enter a number:"))
if 1 <= num <= 9:
    print("Single Digit number")
elif 10 <= num <= 99:
    print("Double Digit Number")
elif 100 <= num <= 999:
    print("Three Digit Number")
elif num == 1000:
    print("Four Digit Number")
else:
    print("Number out of range")


# 4 digit number first and last digit equal or not equla

num = int(input("Enter a number:"))
last_digit = num % 10
first_digit = int(str(num)[0])
if first_digit == last_digit:
    print("First and last digits are equal")
else:
    print("First and Last digits are not equal")

# 

mark = int(input("Enter a mark:"))
if mark <= 90:
    print("A+ grate")
elif 80 >= mark <= 89:
    print("A grate")
elif 70 >= mark <= 79:
    print("B+ great")
elif 60 >= mark <= 69:
    print("B grate")
elif 50 >= mark <= 59:
    print("C grate")
else:
    print("fail")

# 21/05/2026 Leap year or not leap year

n = int(input("Enter a year:"))
if n%4 == 0 and n % 100!= 0 or n%400 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# Geometry Based !)

a = int(input())
b = int(input())
c = int(input())

if a+b > c or b + c > a or a + c > b:
    if a==b and b==c:
        print("Equilateral")
    elif a==b or b==c or a==c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a vaild triangle")



"""
unit 500
0 -100 ->free
100-300 ->5rs per unit
300-500 -> 10rs per unit
>500 15rs per unit

>500 Apply extre charges -> 500rs
450 - 100 -> 350

""" 

units = int(input())
bill = 0
if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
elif units <= 500:
    bill = (200) * 5 + (units - 300) * 10
else:
    bill = (200) * 5 + (200)*10 + (units-500) * 25+500
print(bill)
# year based 5)

n = int(input())
"""
month == 2
    leap year condition
        month = 2 -> 29
    else:
        28
1,3,5,7,8,10,12 - > 31

else: 30
"""

# range(start ,  stop, step)

l =range(2,10,3)
for i in l:
    print(i,end = ' ')

# 2)
 
n = int(input())
sum = 0
for i in range(1,n+1):
    sum += 1
print(sum)

# 3)Factor number

n = int(input())
fact = 0
for i in range(1, n+1):
    fact *= i
print(fact)

# 4) Faboserie

n = int(input())
a = 0
b = 1
print(a,b,end =" ")
for i in range(2,n+1):
    c =a + b
    print(c , end = " ")
    a = b
    b = c  
    # 0 1 1 2 3 5 8 13

#6) prime number

n = int(input())
count = 0 
for i in range(1,n+1):
    """
    (2,n//2)
    """
    if n%i == 0 :
        count += 1
if count == 2:
    print("Prime ")
else:
    print("Not prime")



#  given number is fact
n = int(input())
for i in range(1,n+1):
    if n%i == 0:
        print(i, end = " ")

#  write a program print alpehate from a to z

# 25/05/2026

# 1)while loop

n = int(input())
count= 0
if n==0:
    count = 1
elif n < 0:
    n = -n
while n!=0:
    count += 1
    n//=10
print(count)

# 2)Reveser

n = int(input())
res = 0 
while n!=0:
    last = n % 10 
    res = res * 10 + last
    n//=10
print(res)

# 3)frist digit to get

n =int(input())
while n > 9:
    n //= 10
print(n)

# 4)give number check the number how many time reptred

n = int(input())
digit = int(input())
count = 0
while n!=0:
    if n%10 == digit:
        count += 1
    n//=10
print(count)

# 5)check the number ascender order or descend order

n = int(input())
prev = 10
while n!= 0 :
    curr = n%10
    if prev < curr:
        print(False)
        # exit()
        break
    prev = curr
    n //= 10
print(True)
# output :1234 True

# 6)Find the maxima  number in give number
'''
n =int(input())
maximum = n[0]
i = 0
while i < len(n):
    if n[i] > maximum:
        maximum = n[i]
    i += 1
print("Maximum number:",maximum)

'''
n =int(input())
max = 0
while n!=0:
    if n%10 > max:
        max = n% 10
    n //= 10
print(max)


# 7)Check whether numbers are Even , odd ,or mixed

n = int(input())
even_count = 0
odd_count = 0 
while n!= 0:
    if (n%10)%2 == 0:
        even += 1
    else:
        odd += 1
if even > 0 and odd == 0:
    print("Even Number")
elif even == 0 and odd > 0:
    print("Odd Number")
else:
    print("Mixed number")







