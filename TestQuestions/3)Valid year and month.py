# 3)Valid year and month

year = int(input("Enter a year:"))
month = int(input("Enter a month(1 to 12):"))

if month < 1 or month > 12:
    print("Invaild Month")

else:
    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print("29 days")
        else:
            print("28 days")
    elif month in [4,6,9,11]:
        print("30 days")
    else:
        print('31 days')

# 4)Grade calculaction 

marks = int(input("Enter your marks:"))
if marks>= 90:
    print('A')
elif marks >= 75:
    print('B')
elif marks >= 50:
    print('C')
else:
    print('Fail')

# 5)Electricity bill calculation

units = int(input("Enter the units :"))
if units < 100:
    bill = 0
elif units <= 300:
    bill = (units -100)*5
else:
    bill = (200*5)+((units-300)*10)

if units > 500:
    bill = bill +(bill *0.10)
print("Electricity bill is:",bill)

# 6)Find the product od digits of a number

n = int(input("Enter a number:"))
product = 1
while n >0:
    digit = n % 10
    product = product * digit
    n = n // 10
print("Product of digits is:",product)

# 7)Find the sum of factors of a number

n = int(input("Enter the number"))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print("Sum of Factors is:",sum)

# 8)Covert decimal to binary 

n = int(input("Enter a decimal number:"))
binary = "" 
while n > 0:
    binary = str(n%2) + binary
    n = n// 2
print('Binary',binary)

# 9)The largest digit in a number

n = int(input("Enter a number:"))
largest = 0
while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
        n = n // 10
    print("Largest:",largest)

# 10)All prime numbers from 1 to N

n = int(input("Enter a number:"))
for i in range(2, n+1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        print(i)