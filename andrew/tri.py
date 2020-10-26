import time
time.sleep(1)
print("I am going to do the area for 4 shapes.")
time.sleep(1)
width = int(input("What do what the width of your triangle to be?"))
time.sleep(1)
height = int(input("What do what the height of your triangle to be?"))
time.sleep(1)
size = int(input("What one of the square's side to be?"))
time.sleep(1)
size1 = int(input("What do you what the circle's radius to be?"))
time.sleep(1)
width1 = int(input("What do you what the width of your rectangle to be?"))
time.sleep(1)
height1 = int(input("What do you what the height of your rectangle to be?"))
class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height / 2.0
        return area

class Square:
    def __init__(self, size):
        self.size = size

    def getArea(self):
        area = self.size * self.size
        return area

    def getPre(self):
        pre = self.size + self.size + self.size + self.size
        return pre


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = 3.14 * self.radius * self.radius
        return area

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height
        return area
myTriangle = Triangle(width, height)
mySquare = Square(size)
myCircle = Circle(size1)
myRectangle = Rectangle(width1, height1)
time.sleep(1)
areaTriangle = myTriangle.getArea()
print("Triangle's area: ", areaTriangle)
time.sleep(1)
areaSquare = mySquare.getArea()
print("Square's area: ", areaSquare)
time.sleep(1)
areaCircle = myCircle.getArea()
print("Circle's area: ", areaCircle)
time.sleep(1)
areaRectanlge = myRectangle.getArea()
print("Rectangle's area: ", areaRectanlge)
time.sleep(1)
print("Now I am going to do the perimeter of these 4 shapes.")
time.sleep(1)
tri = int(input("What do you what a side of your triangle to be?"))
class Triangle:
    def __init__(self, size):
        self.size = size

    
class Square:
    def __init__(self, size):
        self.size = size

    
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getPre(self):
        pre = self.radius * 2 * 3.14
        return pre

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getPre(self):
        pre = self.width + self.width + self.height + self.height
        return pre

myTriangle1 = Triangle(tri)
mySquare1 = Square(size)
myCircle1 = Circle(size1)
myRectangle1 = Rectangle(width1, height1)
time.sleep(1)
preTriangle = myTriangle1.getPre()
print("Triangle's perimeter: ", preTriangle)
time.sleep(1)
preSqaure = mySquare1.getPre()
print("Squares's perimeter: ", preSqaure)
time.sleep(1)
preCircle = myCircle1.getPre()
print("Circle's circumference: ", preCircle)
time.sleep(1)
preRectangle = myRectangle1.getPre()
print("Rectangle's perimeter: ", preRectangle)
