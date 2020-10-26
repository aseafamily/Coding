class Triangle:
    def __init__(self, width, height, side1, side2, side3):
        self.width = width
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getArea(self):
        area = self.width * self.height / 2.0
        return area
    def getPeri(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter
class Square:
    def __init__(self, size):
        self.size = size

    def getArea(self):
        area = self.size * self.size
        return area
    def getPeri(self):
        perimeter = self.size * 4
        return perimeter

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = self.radius * self.radius * 3.14
        return area
    def getCircum(self):
        circumference = self.radius * 2 * 3.14
        return circumference
class Rectangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def getArea(self):
        area = self.length * self.height
        return area

    def getPeri(self):
        perimeter = self.length + self.length + self.height + self.height
        return perimeter
    
thewidthft = float(input('What is the width of the triangle?'))
theheightft = float(input('What is the height of the triangle'))
side1ft = float(input('What is the length of the first side of the triangle?'))
side2ft = float(input('What is the length of the second side of the triangle?'))
side3ft = float(input('What is the length of the third side of the triangle?'))
myTriangle = Triangle(thewidthft, theheightft, side1ft, side2ft, side3ft)

thesidefs = float(input("What is the length of one of the square's sides?"))
mySquare = Square(thesidefs)

theradiusfc = float(input('What is the radius of the circle?'))
myCircle = Circle(theradiusfc)

thelengthfr = float(input('What is the height of the rectangle?'))
theheightfr = float(input('What is the length of the rectangle?'))
myRectangle = Rectangle(thelengthfr, theheightfr)

areaOfTriangle = myTriangle.getArea()
areaOfSquare = mySquare.getArea()
areaofCircle = myCircle.getArea()
areaofRectangle = myRectangle.getArea()
periofTriangle = myTriangle.getPeri()
periofSquare = mySquare.getPeri()
circumofCircle = myCircle.getCircum()
periofRectangle = myRectangle.getPeri()
print('The area of the triangle is ' + str(areaOfTriangle))
print('The perimeter of the triangle is ' + str(periofTriangle))
print('The area of the square is ' + str(areaOfSquare))
print('The perimeter of the square is ' + str(periofSquare))
print('The area of the circle is', str(areaofCircle))
print('The circumference of the circle is ' + str(circumofCircle))
print('The area of the rectangle is ' + str(areaofRectangle))
print('The perimeter of the rectangle is ' + str(periofRectangle))
