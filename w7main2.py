import turtle
t1=turtle.Turtle()
wn=turtle.Screen()
size=50
pos=(0,0)
def drawSquareAt(size,pos):
    tracks=list()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.fd(50)
        t1.right(90)
        tracks.append(t1.pos())
        return tracks
    
def lab7():
    drawSquareAt(size,pos)
    print mytracks
def main():
    lab7()
main()
