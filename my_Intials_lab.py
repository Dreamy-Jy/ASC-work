'''
By Jordane Thomas, Goldman Sach 2016 ASC Cohort
7/13/2016
code your intial lab
'''

from Myro  import *

init('sim')
penDown()

def drawJ():
    forward(1, .5)
    backward(1,1)
    forward(1, .5)
    turnBy(-90,"deg")
    forward(1,1)
    turnBy(-90,"deg")
    forward(1,.5)

def drawT():
    forward(1,1)
    turnBy(90,"deg")
    foward(1,.5)
    backward(1,1)
    

drawJ()
penUp()
turnBy(180, "deg")
forward (1,1.5)
turnBy(90,"deg")
penDown()
drawT()