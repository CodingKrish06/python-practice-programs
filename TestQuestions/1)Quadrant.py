X = int(input("Enter the value of X:"))
Y = int(input("Enter the value of Y:"))

if X > 0 and Y > 0:
    print("First Quadrant")

elif X < 0 and Y < 0:
    print("Second Quadrant")
elif X < 0 and Y < 0:
    print("Third Quadrant")
elif X > 0 and Y < 0 :
    print("Fourth Quadrant")
elif X == 0 and Y == 0:
    print("Origin")
elif X == 0:
    print("Y axis")
else :
    print("X axis")