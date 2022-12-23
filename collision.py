import pygame, random

pygame.init()
screenWidth, screenHeight = 800, 800
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Collision')

BG = (157, 184, 218)
window.fill(BG)

COLOR1 = (218, 91, 71)
radius1 = 30
x1 = random.randint(31, 769)
y1 = random.randint(31, 769)
xVel1 = 10
yVel1 = 9

COLOR2 = (72, 255, 150)
radius2 = 30
x2 = random.randint(31, 769)
y2= random.randint(31, 769)
xVel2 = -12
yVel2 = -13

class Circle():
    def __init__(self, radius, win, x, y, xVel, yVel, color):
        self.radius = radius
        self.win = win
        self.x = x
        self.y = y
        self.xVel = xVel
        self.yVel = yVel
        self.color = color

    def drawCircle(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        pygame.display.update()

    def moveCircle(self, win):
        self.x += self.xVel
        self.y += self.yVel
        win.fill(BG)

        if self.x + self.radius >= screenWidth or self.x - self.radius <= 0:
            self.xVel = -self.xVel
        if self.y + self.radius >= screenHeight or self.y - self.radius <= 0:
            self.yVel = -self.yVel

    @staticmethod
    def checkCollision(c1: object, c2: object, window):
        length = c2.x - c1.x
        breadth = c2.y - c1.y
        distance = round((length**2 + breadth**2)**0.5)

        if distance <= c1.radius + c2.radius:
            c1.xVel = -c1.xVel
            c1.yVel = -c1.yVel
            c2.xVel = -c2.xVel
            c2.yVel = -c2.yVel

clock = pygame.time.Clock()
circle1 = Circle(radius1, window, x1, y1, xVel1, yVel1, COLOR1)
circle2 = Circle(radius2, window, x2, y2, xVel2, yVel2, COLOR2)
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    circle1.drawCircle(window)
    circle2.drawCircle(window)
    circle1.moveCircle(window)
    circle2.moveCircle(window)
    Circle.checkCollision(circle1, circle2, window)