import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
nBigger=2
for i in range(0,10):
    if(i%nBigger):
        print i
def makeSwirlSquare(size):
    sides=10
    bigger=10
    angle=90
    t1.home()
    t1.clear()
    for i in range(0,sides):
        if(i%2):
            
            size=size+bigger
            #size+=bigger
            t1.fd(size)
            t1.right(angle)
makeSwirlSquare(10)  

wn.exitonclick()