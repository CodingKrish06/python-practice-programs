# 1)two_sum
a= int(input("Enteer the A number:"))
b = int(input("Enter the B number:"))
sum = a + b
print("The sum of a and b :",sum,sep="")
# 2)two_different
sub = a - b
print("The different of two number:",sub,sep="")
# 3)two_product
mul = a * b
print("The product of two number:",mul,sep="")

# 4)QUOFICIENT
A = int(input("Enter A value:"))
B = int(input("Enter B value:"))
quoficient = A // B
print("Quoficient is:",quoficient)

# 5)REMAINDER
remainder = A % B
print("Remainder is:",remainder)

# 6)USING THIRD VARIABLE

A = int(input("Enter the A number:"))
B = int(input("Enter the B number:"))
temp = A
A = B
B = temp
print("After Swapping :",A, B)

#7)WITHOUT USING THIRD VARIABLE
A = A + B
B = A - B
A = A - B
print("After Swapping A and B:",A,B)

#Print the last Didit of given number
num = int(input("Enter a number:"))
last_digit = num % 10
print("Last digit:",last_digit)

#print all digits except last digit

remaining = num // 10
print("Digits except last digit:",remaining)

# 10)Print sum of first an dlast digit of a 3-digit number

num = int(input("Enter a 3-digit number:"))
first_digit = num // 100
last_digit = num % 10
sum_digits = first_digit + last_digit
print("Sum of first and last digit:",sum_digits)

# 11)Print the Middle Digit of a 3-digit Number

num = int(input("Enter a 3-digit number:"))
middle_digit = (num // 10) % 10
print("Middle digit:",middle_digit)


#12)Print Absolute value of a Number
numbers = list(map(int, input("Enter numbers separated by space:").split()))
absolute_values = list(map(abs, numbers))
print("Absolute values:", absolute_values)

# 13)Print Square of a Number

num = int(input("Enter a number:"))
square = num ** 2
print("Square:",square)

#14) print cube of a number

num = int(input("Enter a number:"))
cube = num ** 3
print("Cube:",cube)

#15)Calculate Average of Three Numbers

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
average = (a+b+c)/3
print("Average:",average)

#16)Check whether Two Numbers are Equal

a = int(input("Enter frist number:"))
b = int(input("Enter second number:"))
if a == b:
    print("Two numbers are equal")
else:
    print("Two numbers are not equal")

#17)Check if a Number is power of 2 Using Bitwise AND

num = int(input("Enter a number:"))
if num > 0 and (num & (num-1)) == 0:
    print("True")
else:
    print("False")

#18)Check Whether Number is positive or Negative

num = list(map(int,input("Enter the number:").split()))
if num >= 0:
    print(f"Given number is {num} positive")
else:
    print(f"Given number is {num} negative")


#19) Find greatest of Three Numbers

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a >= b and a >= c:
    print("A is Greatest number:",a)
elif b >= a and b >= c:
    print("B is Greatest number:",b)
else:
    print("C is Greatest number:",c)

#20)Print Pass/Fail result Based on Marks

marks = list(map(int,input("Enter the Mark:").split()))
if marks >= 35:
    print("Pass")
else:
    print("Fail")
