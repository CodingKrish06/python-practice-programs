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
print("Alice must go in path-" + str(digit_sum))

# 4) Simple Interest

principal_amount = int(input())
Year = int(input())
rate_interest = float(input())
Simple_interest = principal_amount * Year * rate_interest / 100
print(f"{Simple_interest:.2f}")

# 5)Midpoint of a Line Segment

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2
print(f"Binoy's house is located at ({mid_x},{mid_y})")

# 6)

students = int(input())
teams = int(input())
per_team = students // teams
left_out = students % teams
print(f"The number of students in each team is {per_team} and left out is {left_out}")

# 7)

books = int(input())
students = int(input())
each_student = books // students
remaining = books % students
print(f"Each student gets {each_student} books and {remaining} books remain in the library")

# 8)

n = int(input())
teams = n // 11
referes = n % 11 
print(teams)
print(referes)

# 9)

N = int(input())
X = int(input())
Y = int(input())
Z = int(input())
A = (Z - N * Y) // (X - Y)
B = N - A
print(A)
print(B)

# 10)


