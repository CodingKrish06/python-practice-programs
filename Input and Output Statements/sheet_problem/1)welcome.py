# 1)welcome

print("Welcome")

# 2)word.py

word = input("Enter the word:")
print(word)

# 3)message

message = input("Entter the message")
print(message)

# 4)integer

a = int(input("Enter the number:"))
print(a)

# 5)Fractional_number

number = float(input("Enter a fractional number: "))
print("The fractional number is:", number)

# 6) Fractional_number

number = float(input("Enter a fractional number:"))
print("Formatted number:{:.2f}".format(number))

# 7)Int_Hexdecimal

number = int(input("Enter an integer number:"))
print("Hexadecimal format:",hex(number))

# 8)Int_Octal

number = int(input("Enter an integer number:"))
print("Octal formatt:",oct(number))

# 9) Hexdecimal_int

hex_num = input("Enter a hexadecimal number: ")
print("Integer format:",int(hex_num,16))

# 10)Octal_Int

oct_num = input("Enter an octal number:")
print("Integer format:",int(oct_num,8))

# 11)Char_ASCII

ch = input("Enter a character:")
print("ASCII value is:",ord(ch))

# 12)ASCII_Char

ascii_value = int(input("Enter ASCII value:"))
print("Character is:",chr(ascii_value))

# 13)Space_between

a = int(input("Enter the A value:"))
b = int(input("Enter the B value:"))
print("A and B value:",a, b)

# 14)TabSpace_between

a = int(input("Enter the A value:"))
b = int(input("Enter the B value:"))
print("A and B value is:",a,"\t",b)

# 15)TwoNum_twoLine

num1= int(input("Enter the num1:"))
num2 = int(input("Enter the num2:"))
print("Number1:",num1)
print("Number2:",num2)

# 16)Char_sinlgequote

ch = input("Enter the Character:")
print("Character is:","'" + ch + "'")

# 17)Twowrods_DoubleQuotes

word1 = input("Enter first word:")
word2 = input("Enter second word:")
print(f'"{word1}" "{word2}"')

# 18)DOB

day = int(input("Enter day:"))
month = int(input("Enter month:"))
year = int(input("Enter year:"))
print("Data of Birth:",f"{day:02d}/{month:02d}/{year}")

# 19) Plus_sign

num = int(input("Enter a number:"))
print(f"{num:+}")

# 20)char_int_float_double

char = input("Enter a character:")
integer = int(input("Enter an integer value:"))
floating = float(input("Enter a float value:"))
double_value = float(input("Enter a double value:"))
print("Type of char:",type(char))
print("Type of int:",type(integer))
print("Type of float:",type(floating))
print("Type of double:",type(double_value))

# 21)RollNum_Name

roll_no = input("Enter the Roll number:")
Name = input("Enter the Name:")
print(f"Roll number:{roll_no}, Name:{Name}")

# 22)fiveSub_mark

Tamil = int(input("Enter the Tamil Mark:"))
English = int(input("Enter the English Mark:"))
Maths = int(input("Enter the Maths Mark:"))
Computer = int(input("Enter the Computer Mark:"))
Social = int(input("Enter the Social Mark:"))
print("Tamil mark is:",Tamil)
print("English mark is:",English)
print("Maths mark is:",Maths)
print("Computer mark is:",Computer)
print("Social mark is:",Social)

# 23)Blood_Group
blood_group = input("Enter your Blood group:")
print("Blood Group:",blood_group)

# 24)HH_MM_SS
hour = input("enter hour:")
minute = input("Enter minute:")
second = input("Enter Second:")
print(hour + ":" + minute + ":" + second)

# 25)Address

street = input("Enteer street name:")
city = input("Enteer city:")
state = input("Enter state:")
country = input("Enter country:")
print(street + "\n" + city + "\n" + state + "\n" + country)