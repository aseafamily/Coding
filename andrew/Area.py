import time

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

    def getPre(self):
        pre = self.radius * 2 * 3.14
        return pre

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height
        return area

    def getPre(self):
        pre = self.width + self.width + self.height + self.height
        return pre


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
preSqaure = mySquare.getPre()
print("Squares's perimeter: ", preSqaure)


time.sleep(1)
areaCircle = myCircle.getArea()
print("Circle's area: ", areaCircle)
time.sleep(1)
preCircle = myCircle.getPre()
print("Circle's perimeter: ", preCircle)
areaRectanlge = myRectangle.getArea()
print("Rectangle's area: ", areaRectanlge)
time.sleep(1)
preRectangle = myRectangle.getPre()
print("Rectangle's perimeter: ", preRectangle)