import turtle as t


def ping(x,y):

    turtlepos[2] = 1
    turtlepos[0] = 3
    turtlepos[3] = 30


turtlepos = [0,0,0,0]
t.speed(0)
t.screensize(2000,2000,'white')
t.penup()
t.shape("circle")
# t.setup( width = 600, height = 600, startx = None, starty = None)
t.setup(800, 600)
running = True
t.Screen().onclick(ping)
while running:
    if turtlepos[2] == 1:
        if turtlepos[3] > 0:
            turtlepos[0] -= 0.1
            turtlepos[1] += turtlepos[0]
            turtlepos[3] -= 1
        else:
            turtlepos[2] = 0
            turtlepos[0] = 0
    else:
        turtlepos[1] -= turtlepos[0]
        turtlepos[0] += 0.1

    t.goto(0,turtlepos[1])


