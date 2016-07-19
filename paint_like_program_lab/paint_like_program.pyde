"""
By Jordane Thomas, Goldman Sach 2016 ASC Cohort
7/18/2016
Paint Copy lab
"""
def setup():
    size(600,600)
    background(255)
    makeOptions()
def draw():
    if mouseY <= 120:
        select()
    else:
        if mousePressed == True:
            noStroke()
            rect(mouseX,mouseY, 10,10)
def makeOptions():
        
    fill(0,0,0) #black
    rect(0,0,75,120)
    
    fill(255,255,255) #white
    rect(75,0,75,120)
    
    fill(128,128,128) #grey
    rect(2*75, 0, 75,120)
    
    fill(255,0,0) #red
    rect(3*75,0,75,120)
    
    fill(0,255,0) #green
    rect(4*75,0,75,120)
    
    fill(0,0,255) #blue
    rect(5*75,0,75,120)
    
    fill(255,215,0) #maroon
    rect(6*75,0,75,120)
    
    fill(128,0,0) #gold
    rect(7*75,0,75,120)    

def select():
    if mousePressed == True:
        if mouseX < 75:
            fill(0,0,0) #black
        elif mouseX < 2*75:
            fill(255,255,255) #white
        elif mouseX < 3*75:
            fill(128,128,128)#grey
        elif mouseX < 4*75:
            fill(255,0,0) #red
        elif mouseX < 5*75:
            fill(0,255,0) #blue
        elif mouseX < 6*75:
            fill(0,0,255) #green
        elif mouseX < 7*75:
            fill(255,215,0) #maroon
        elif mouseX < 8*75:
            fill(128,0,0) #gold