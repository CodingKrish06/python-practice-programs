# 1)Positive ,Negative or Zero - Bank Balance Status

N = int(input())
if N >= 0 :
    print("Positive")
elif N <= 0 :
    print("Negative")
else:
    print("Zero Balance")

# 2) Even or Odd - Token Number Checker

N = int(input())
if N % 2 == 0:
    print("Even")
else:
    print("Odd Token")

# 3)Pass or Fail - Student Result Checker

M = int(input())
if M >= 35:
    print("Pass")
else:
    print("Fail")

# 4)Largest of Two Numbers = Price Comparison

A, B = map(int,input().split())

if A > B:
    print("A is Costier")
elif A < B:
    print("B is Costier")
else:
    print("Equal prices")

# 5)Largest of Three Numbers - Score Winner

A, B, C = map(int,input().split())
if A == B == C:
    print("Tie")
elif A > B and A > C:
    print("Player A")
elif B > A and B > C:
    print("Player B")
else:
    print("Player C")


# 6)Vowel or Consonant - Character Classifier

ch = input()
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else:
    print("Consonant")


# 7)Leap Year Checker - Calendar System

year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year")
else:
    print("Not Leap Year")


# 8) Age Category - Ticket Pricing System

age = int(input())
if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen")
elif age >= 20 and age <= 59:
    print("Adult")
else:
    print("Senior Citizen")

# 9)Simple Calculator

A, B ,op = input().split()
A = int(A)
B = int(B)
if op == '+':
    print(A + B)
elif op == '-':
    print(A - B)
elif op == '*':
    print(A * B)
elif op == '/':
    print(A // B)
else:
    print("Invalid Operator")

# 10)Triangle Validity - Construction check

A, B, c = map(int,input().split())
if (A + B > c) and (A + c > B) and (B + C > A):
    print("Valid Triangle")
else:
    print("Invalid Triangle")

# 11)Grade Calculator - Exam Report

M = int(input())
if M >= 90 and M<= 100 :
    print("A")
elif M >= 75 and M <= 80:
    print("B")
elif M >= 60 and M <= 74:
    print("C")
elif M >= 35 and M <= 50:
    print("D")
else:
    print("F")

# break -> 

n = int(input())
for i in range(n+1):
    print(i,end="")
    if i == 10:
        break
    print("Hello word")


# Continue 
n = int(input())
for i in range(n+1):
    if i % 2 != 0:
        continue
    print(i,end='')