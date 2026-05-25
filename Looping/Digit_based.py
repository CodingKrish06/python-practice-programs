# 13)Remove all zeroes from a given number
num = int(input())
result = ""
i = 0
while i < len(num):
    if num[i] != '0':
        result += num[i]

    i += 1
print(result)