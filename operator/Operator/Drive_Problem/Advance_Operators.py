# 1) Calculate Area of Square,Rectangle and Circle

a = int(input("Enter a square:"))
length = int(input("Enter the length:"))
breadth = int(input("Enter the breadth:"))
radius = float(input("Enter the radius:"))
square  = a ** 2
rectangle = length * breadth
circle = 3.14 * radius ** 2
print("Area of Square:",square)
print("Area of Rectangle:",rectangle)
print(f"Area of Circle:{circle:.2f}")

# 2)Power 

X = int(input("Enter a base:"))
N = int(input("Enter a power:"))
c = X ** N
print(c)

#  3)

n = int(input())
digit_sum = (n // 10) + (n % 10)
print(str(digit_sum))

# 4) Simple Interest

principal_amount = int(input())
Year = int(input())
rate_interest = float(input())
Simple_interest = principal_amount * Year * rate_interest / 100
print(f"{Simple_interest:.2f}")