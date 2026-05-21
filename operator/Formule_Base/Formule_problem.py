# 1)Find area of Rectangle

length = float(input("Enter length:"))
breadth = float(input("Enter breadth"))
area = length * breadth
print("Rectangul :")

# 2)Find area of square

side = float(input("Enter Side:"))
area = side * side
print("Area of Square:",area)

# 3)Find area of Trianlge

base = float(input("Enter a base value:"))
height = float(input("Enter a height value:"))
area = 1/2 * base * height
print("Triangle:",area)

# 4)Find area of circle

radius = float(input("Enter radius:"))
area = 3.14 *radius * radius
print("Area of circle:",area)

# 5)Find the distance between two points

x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))
distance = ((x2 - x1)** 2 + (y2 -y1) ** 2) ** 0.5
print("Distance:",distance)

# 6)Calculate Fahrenheit to Celsius

fahrenheit = float(input("Enter temperature in Fahrenheit"))
celsius = (fahrenheit - 32) * 5 / 9
print("Celsius:",celsius)


# 7)Calculate Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius:"))
fahrenheit = (celsius * 5 / 9) + 32
print("Fehrenheit:",fahrenheit)

# 8)Find Perimeter of a Square

side = float(input("Enter side of square"))
perimeter = 4 * side
print("Perimeter of square:",perimeter)

# 9)Find Perimeter of a rectangle

length = float(input("Enter length:"))
breadth = float(input("Enter breadth:"))
perimeter = 2 * (length * breadth)
print("Perimeter of Rectangle:",perimeter)

# 10)Find Perimeter of Triangle

a = float(input("Enter A value:"))
b = float(input("Enter B value:"))
c = float(input("Enter C value:"))
perimeter = a + b + c
print("Perimeter of Triangle:",perimeter)

# 11)Find Circumference of a Circle

radius = float(input("Enterr radius:"))
pi = 3.14
circumference = 2 * pi * radius
print("Circumference of Circle:",circumference)

# 12)Find Surface Area, Volume and Perimeter of Cube

side = float(input("Enter side of cube:"))
surface_area = 6 * side * side
volume = side ** 3
perimeter = 12 * side
print("Surface Area:",surface_area)
print("Volume:",volume)
print("Perimeter:",perimeter)

# 13)Find Surface Area and Volume of Cuboid

length = float(input("Enter length:"))
breadth = float(input("Enter breadth:"))
height = float(input("Enter height:"))
surface_area  = 2 * (length * breadth + breadth * height + height*length)
volume = length * breadth * height
print("Surface Area:", surface_area)
print("Volume:",volume)

#14) Find Surface Area and Volume of Sphere

radius = float(input("Enter raduis:"))
pi = 3.14
surface_area = 4 * pi * radius * radius
volume = (4/3) * pi * radius ** 3
print("Surface Area:",surface_area)
print("volume:",volume)

# 15) Find Surface Area and Volume of Cylinder

radius = float(input("Enter radius:"))
height = float(input("Enter height:"))
pi = 3.14
surface_area = 2 * pi * radius *(radius + height)
volume = pi * radius * radius * height
print("Surface Area:",surface_area)
print("Volume:",volume)

