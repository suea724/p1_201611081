import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
import math
def isInCircle(center,radius,pos):
    return 0<math.sqrt(math.pow(center[0]-pos[0],2) + math.pow(center[1]-pos[1],2))<radius

def Circle((x,y),size):
    t1.setpos(x,y)
    t1.setheading(0)
    t1.fillcolor("Orange")
    t1.begin_fill()
    t1.circle(size)
    t1.end_fill()
def isInRectangle(curpos,coord):
    xs=coord[0][0]
    xe=coord[1][0]
    ys=coord[0][1]
    ye=coord[1][1]
    return xs<=curpos[0]<=xe and ys<=curpos[1]<=ye
def Sqr1((x,y),size):
    angle = 90
    t1.fillcolor("Pink")
    t1.begin_fill()
    t1.setpos(x,y)
    t1.setheading(0)
    for i in range(4):
        t1.forward(size)
        t1.right(angle)
    t1.end_fill()

def Sqr2((x,y),size):
    angle = 90
    t1.setpos(x,y)
    t1.setheading(0)
    for i in range(4):
        t1.forward(size)
        t1.right(angle)

def initialize():
    t1.clear()
    t1.setpos(100,0)
    t1.Circle(100)
    Sqr2((0,0),100)

def keyup():
    pos=t1.pos()
    t1.forward(45)
    if isInRectangle((pos),[(0,-100),(100,0)]):
        Square((0,0),100)
    if isInCircle((100,100),100,pos):
        Circle((100,0),100)

def keyleft():
    t1.left(45)

def keyright():
    t1.right(45)

def keydown():
    pos=t1.pos()
    t1.back(45)
    if isInRectangle((pos),[(0,-100),(100,0)]):
        Sqr1((0,0),100)
    if isInCircle((100,100),100,pos):
        Circle((100,0),100)

    
def addKeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keyleft, "Left")
    wn.onkey(keyright, "Right")
    wn.onkey(keydown, "Down")
     
def mousegoto(x,y):
    t1.setpos(x,y)
    pos=t1.pos()
    if isInRectangle((x,y),[(0,-100),(100,0)]):
        Sqr1((0,0),100)
    if isInCircle((100,100),100,pos):
        Circle((100,0),100)

def addMouse():
    wn.onclick(mousegoto)
    
def gamePlay():
    initialize()
    addKeys()
    addMouse()
    wn.listen()
    turtle.mainloop()


def lab11():
    gamePlay()

lab11() 
