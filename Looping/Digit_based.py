# 13)Remove all zeroes from a given number
num = input("Enter a number:")
result = ""
i = 0
while i < len(num):
    if num[i] != '0':
        result += num[i]

    i += 1
print("Number after removing zeroes:", result)