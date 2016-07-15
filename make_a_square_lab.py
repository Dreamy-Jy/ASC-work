'''
By Jordane Thomas, Goldman Sach 2016 ASC Cohort
7/12/2016
Make a square with bot lab
'''

from Myro import *

init('sim')
line_length = 2

for i in range(0,4):
    forward(1,line_length)
    turnBy(90,"deg")