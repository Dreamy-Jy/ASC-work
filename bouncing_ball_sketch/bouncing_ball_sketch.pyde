"""
By Jordane Thomas, Goldman Sach 2016 ASC Cohort
7/19/2016
Bouncing Ball lab
"""

from time import sleep
from random import randint

ballX = 0
ballY = 0
ballSize = 30
velX = randint(-3,3)
velY = randint(-3,3)

def setup():
    global ballX, ballY
    size(600,600)
    print (width," ",height) #temp
    background(255)
    ballX = width/2
    ballY = height/2

def draw():
    global ballX,ballY,ballSize
    print(ballX," ",ballY," ",ballSize)#temp
    background(255)
    fill(128,0,128)
    ellipse(ballX, ballY, ballSize, ballSize)
    moveBy()


def moveBy():
    global velX,velY,ballX,ballY, ballSize
    
    if ballX <= 0 + ballSize/2:
        velX = -1 * velX
    if ballX >= height - ballSize/2:
        velX *= -1

    if ballY <= 0 + ballSize/2:
        velY *= -1    
    if ballY >= width - ballSize/2:
        velY *= -1
    
    ballX += velX
    ballY += velY