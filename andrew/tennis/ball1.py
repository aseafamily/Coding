class Ball:

    
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        msg = "Hi, I'm a " + self.size + " " + self.color + " ball!"
        return msg
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

    def inflate(self):
        if self.size == "small":
            self.size = "big"

    def deflate(self):
        if self.size == "big":
            self.size = "small"

myball = Ball("red", "small", "down")
print("I just created a ball.")
print("My ball is", myball.size)
print("My ball is", myball.color)
print("My ball's direction is", myball.direction)
print("Now I'm going to bounce the ball")
print()
Ball.bounce(myball)
print("Now my ball's direction is", myball.direction)
print(myball)
myball.inflate()
print(myball)
myball.deflate()
print(myball)

