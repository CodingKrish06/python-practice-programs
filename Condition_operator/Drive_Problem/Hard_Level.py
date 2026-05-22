# Income Tax Classifier - Smart Salary System
a = int(input())
i = int(input())
tax = 0 
if a < 60:
    if i > 250000 and i <= 500000:
        tax = (i - 250000) * 5 // 100
    elif i > 500000 and i < 1000000:
        tax = (i - 500000) * 20//100 + 112500
else:
    if i > 300000 and i <= 500000:
        tax = (i -500000) * 5 // 200
    elif i > 500000 and i <= 1000000:
        tax = (i - 500000) * 20//100 + 10000
    else:
        tax = (i - 1000000) * 30//100 + 110000
print(tax)
