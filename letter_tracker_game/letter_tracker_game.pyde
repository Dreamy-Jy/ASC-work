"""
Jordane and Ahnaf
"""

from time import *
from random import choice, randint


currentLetters= [ #holds the values ([chr][x][y]) for x val and y val 
                 [chr(randint(97,121)) ,-10 ,10 * randint(2,49)],
                 [chr(randint(97,121)) ,-30 ,10 * randint(2,49) ],
                 [chr(randint(97,121)) ,-60 ,10 * randint(2,49) ],
                 [chr(randint(97,121)) ,-90 ,10 * randint(2,49) ]
                 ]
velx = 5
def setup():
    size(500,500)
    background(255)

def draw():
    global currentLetters,velx
    background(255)
    fill(0)
    createLetter()
    textAlign(LEFT,LEFT)
    textSize(25)
    for i in range(len(currentLetters)):
        text(currentLetters[i][0],currentLetters[i][1],currentLetters[i][2])
        
    for i in range(len(currentLetters)):
        currentLetters[i][1] += velx
    
    if currentLetters[i][1] == width:
            currentLetters.remove(currentLetters[i])
    
    #sleep(1)
    
def createLetter():
    global currentLetters
    if len(currentLetters) < 4:
        letter = chr(randint(97,121))
        y = choice([ 100, 300, 400, 500])
        #while any(y in currentLetters):
            #y = choice([0, 100, 300, 400])
        x = 0
        currentLetters.append([letter, x, y])

def keyPressed():
    global currrentLetters
    
    if key == currentLetters[0][0]:
        currentLetters.remove(currentLetters[0])
    