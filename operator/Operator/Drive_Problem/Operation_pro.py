# 1)program to perform arithmetic operations such as addition, subtraction,multiplication, modulo division and division.

a, b = map(int, input("Enter two numbers separated by space:").split())
print("Addition:",a + b)
print("Subtraction:",a - b)
print("Multiplication:",a * b)
print("Modulo Division:",a % b)
print("Division:",a // b)

# 2)Find Rope Length and Carpet Area

length, breadth = map(int,input("Enter length and breadth:").split())
rope_length = 2 * (length * breadth)
carpet_area = length * breadth
print("Rope length:",rope_length)
print("Carpet area:",carpet_area)

# 3)Program to Calculate Interest, Amount, Discount and Final Settlement

principal = int(input("Enter principal amount:"))
rate = int(input("enter rate of interest:"))
years = int(input("Enter number of years:"))
interest = (principal * rate * years) / 100
amount = principal + interest
discount = interest * 2 / 100
final_settlement = amount - discount
print(f"Interest: {interest:.2f}")
print(f"Amount: {amount:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Settlement: {final_settlement:.2f}")

# 4)Program to Split Students into Teams

students = int(input("Enter number of students:"))
teams = int(input("Enter number of teams:"))
students_per_team = students // teams
left_out = students % teams
print("Students in each team:", students_per_team)
print("Left out students:", left_out)

# 5)Find Midpoint of Two Coordinates

x1 = int(input("Enter X1:"))
y1 = int(input("Enter Y1:"))
x2 = int(input("Enter X2:"))
y2 = int(input("Enter Y2:"))
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2
print(f"{mid_x:.1f} {mid_y:.1f}")

# 6)calculate Newspaper Agency Profit

w = int(input("Enter number of copies sold:"))
x = int(input("Enter selling price per copy:"))
y = int(input("Enter cost price per copy:"))
profit = (w * x) - (w * y) - 100
print(profit)

# 7)Find sum of digits of a two-digit number

num = int(input("Entter a two-digit number:"))
first_digit = num // 10
last_digit = num % 10
sum_digits = first_digit + last_digit
print(sum_digits)

# 8) Find the center of the Battlefield 

x = int(input("Enter x-coordinate:"))
y = int(input("Enter y-coordinate:"))
side = int(input("Enter side length:"))
center_x = x + side // 2
center_y = y + side // 2
print(center_x, center_y)

# 9) Find the Equidistant point of a Triangle

x1 = int(input("Enter x1:"))
y1 = int(input("Enter y1:"))
x2 = int(input("Enter x2:"))
y2 = int(input("Enter y2:"))
x3 = int(input("Enter x3:"))
y3 = int(input("Enter y3:"))
x = (x1 + x2 + x3) / 3
y = (y1 + y2 + y3) / 3
print(f"{x:.1f} {y:.1f}")

# 10) Calculate Discount Amount

item1 = float(input("Enter price of item 1:"))
item2 = float(input("Enter price of item 2:"))
discount = float(input("Enter discount percentage:"))
total = item1 + item2
saved = (discount / 100) * total
discounted_price = total - saved
print(f"{total:.2f}")
print(f"{discounted_price:.2f}")
print(f"{saved:.2f}")

# 11)Calculate Treasure Shares

gold_coins = int(input("Enter number of gold coins:"))
ben_percentage = int(input("Enter Ben's share percentage:"))
blackbeard_percentage = int(input("Enter Blackbeard's share percentage:"))

ben_share = (gold_coins * ben_percentage) // 100
remaining = gold_coins - ben_share
blackbeard_share = (remaining * blackbeard_percentage) // 100
remaining_after_blackbeard = remaining - blackbeard_share
other_pirates_share = remaining_after_blackbeard // 3
print(ben_share)
print(blackbeard_share)
print(other_pirates_share)

# 12)Covert days into years,weeks and days

days = int(input("Enter number of days:"))
years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
days_left = remaining_days % 7
print(years)
print(weeks)
print(days_left)

# 13) Add first and last digit of a four digit number

num = int(input("Enter a four digit number:"))
num = abs(num)
last_digit = num % 10
first_digit = num // 1000
result = first_digit + last_digit
print(result)

# 14)Find number of hops

x = int(input("Enter x-coordinate:"))
y = int(input("Enter y-coordinate:"))
x1 = 3
y1 = 4
distance = ((x - x1)**2 + (y - y1)**2 ) ** 0.5
print(int(distance))

# 15)Calculate wind chill factor

t = int(input("Enter temperature:"))
v = int(input("Enter wind velocity:"))
wcf = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
print(f"{wcf:.2f}")
