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

# 6)

str  = input()
arr = str.split()
print(arr)
print(" ".join(arr))

# 7)Replace the one word to anthon word

str = input()
str = str.replace("l","A")
print(str)

# 8)Program reservee without using inbulid function

str = input()
arr = list(str)
print(arr)

start = 0 
end = len(str)-1

while start < end:
    arr[start],arr[end] = arr[end],arr[start]
    start += 1
    end -= 1
rev = "".join(arr)
print(str == rev)

# 9)

str = input()
ch = input()[0]
first = last =-1
for i in range(len(str)):
    if str[i] == ch:
        if first == -1:
            first = i
        last = i
print(first,last)

