#make fourteen fib bubbles
import turtle as t
def penmove(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def circle_at_position_filled(x,y,rad,colour,angle):
    penmove(x,y)
    t.fillcolor(colour)
    t.begin_fill()
    t.circle(rad,angle)
    t.end_fill()
# t.TurtleScreen
t.screensize(5000,5000,'white')
# t.setup( width = 600, height = 600, startx = None, starty = None)
t.setup(1200, 800)
t.speed(0)
def fibubble(n):
    fiblist = [0,1]
    for i in range(0,n):
        fiblist.append(fiblist[i]+fiblist[i+1])
    xcord = -550
    ycord = -325
    for i,v in enumerate(fiblist[0:n]):
        print(f"index value is {i}, and value is {v}")
        circle_at_position_filled(xcord,ycord,v,'blue',360)
        penmove(xcord,ycord+v)
        t.write(v,align = 'center')
        xcord+= fiblist[i+2]
        ycord -= fiblist[i+1] - v
fibubble(15)
t.hideturtle()
t.exitonclick()


