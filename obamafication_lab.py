"""
By Jordane Thomas, Goldman Sach 2016 ASC Cohort
7/18/2016
Obamafication lab
"""
from Myro import *

ObamaDarkBlue = makeColor(0,51,76)
ObamaRed = makeColor(217,26,33)
ObamaBlue = makeColor(112,150,158)
ObamaYellow = makeColor(252,227,166)

picture = makePicture(pickAFile())

for pixel in getPixels(picture):
    
    gray = getGray(pixel)
    
    if gray > 180:
        setColor(pixel,ObamaYellow)
    elif gray >120:
        setColor(pixel,ObamaBlue)
    elif gray > 60:
        setColor(pixel,ObamaRed)
    else:
        setColor(pixel,ObamaDarkBlue)
show(picture)