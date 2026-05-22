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