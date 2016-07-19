"""
By Jordane Thomas, Goldman Sach 2016 ASC Cohort
7/19/2016
Bouncing Ball lab
"""

from time import sleep
from random import randint,choice

ballX = 0
ballY = 0
ballSize = randint(20,45)
velX = 5#choice([-3,-2,-1,1,2,3])
velY = 5#choice([-3,-2,-1,1,2,3])

barHeight = 20
barWidth = 200
barVelX = 10
barX = barHeight
barY = barHeight

def setup():
    global ballX, ballY,barX,barY
    size(600,600)
    print (width," ",height) #temp
    background(255)
    ballX = width/2
    ballY = height/2
    barY  = height - barY - 20

def draw():
    global ballX,ballY,ballSize, barX,barY, barHeight, barWidth
    background(255)
    fill(128,0,128)
    ellipse(ballX, ballY, ballSize, ballSize)
    fill(160,0,0)
    rect(barX, barY , barWidth, barHeight)
    moveBall()

def keyPressed():
    global barVelX,barX,barWidth
    if (keyCode == LEFT) & (barX > 0):
        barX -= barVelX
    if (keyCode == RIGHT) & (barX < width - barWidth):
        barX += barVelX

def moveBall():
    global velX,velY,ballX,ballY, ballSize, barX, barY, barWidth
    
    if ballX <= 0 + ballSize/2:
        velX = -1 * velX
    if ballX >= height - ballSize/2:
        velX *= -1

    if ballY <= 0 + ballSize/2:
        velY *= -1    
    if ballY >= width - ballSize/2:
        velY *= -1
        
    if (ballY+ballSize <= barY) & (ballX < barX & ballX > barX + barWidth ):
        print("black")
    
    ballX += velX
    ballY += velY