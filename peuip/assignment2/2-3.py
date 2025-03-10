x1, y1 = map(float, input("Enter x1 and y1: ").split())
x2, y2 = map(float, input("Enter x2 and y2: ").split())
x= x2-x1
y= y2-y1
distance = (x**2 + y**2)**0.5
print("The distance of the two points is ", distance)