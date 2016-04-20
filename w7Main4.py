import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
#wn.bgpic("C:\\Users\\P400\\Documents\\p161\\asdfg.gif")
def saveTracks():
    t1.shape("turtle")
    t1.pencolor("Red")
    tracks=list()
    t1.goto(-130,150)
    tracks.append(t1.pos())
    t1.goto(-130,120)
    tracks.append(t1.pos())
    t1.goto(25,120)
    tracks.append(t1.pos())
    t1.goto(25,-110)
    tracks.append(t1.pos())
    t1.goto(150,-110)
    tracks.append(t1.pos())
    return tracks
def replayTracks(tracks):
    for i in range(0,len(mytracks)):
        print mytracks[i]
def lab7():
    mytracks=saveTracks()
    replayTracks(mytracks)
    
def main():
    lab7()

main()
