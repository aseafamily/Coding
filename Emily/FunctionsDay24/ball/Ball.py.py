class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction
            
    def bounce(self):
        if self.direction == 'down':
            self.direction = 'up'
    def inflate(self):
        if self.size == 'small':
            self.size = 'big'
    def deflate(self):
        if self.size == 'big':
            self.size = 'small'
    def __str__(self):
        mag = "Hi, I'm a " + self.size + ' ' + self.color + ' ball!'
        return mag
myBall = Ball('red', 'small', 'down')
print('I just created a ball.')
print('My ball is', myBall.size)
print('My ball is', myBall.color)
print("My ball's direction is", myBall.direction)
print("Now I'm going to bounce the ball")
print()
Ball.bounce(myBall)
print("Now the ball's direction is", myBall.direction)
print(myBall)
myBall.inflate()
print(myBall)
myBall.deflate()
print(myBall)
