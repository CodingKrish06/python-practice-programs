# 1)First letter capitalize

str = input()
str = str.capitalize()
print(str)

# 2)count function

str = input()
print(str.count('l'))

# 3)
str = input()
print(str.islower())
print(str.isupper())

# 4)
str = input()
print(str.swapcase())

# 5)Without using upper case to lower case or lower case to upper case

str = input()
res = ""
for i in str:
    if i >= 'A' and  i<= 'Z':
        res += chr(ord(i)+32)
    else:
        res += chr(ord(i)-32)
print(res)

