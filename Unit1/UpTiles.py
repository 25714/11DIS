import turtle as t


def GCD(num1,num2):
    num3 = 1
    while num3 != 0:
        num3 = num1%num2
        num1 = num2
        num2 = num3
    return(num1)


def mysqaure(s):
    for i in range(4):
        t.forward(s)
        t.right(90)
def ping(x,y):

    turtlepos[2] = 1
    turtlepos[0]  = 0


turtlepos = [0,0,0]
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
        turtlepos[0] = 3
        for i in range(30):
            turtlepos[0] -= 0.1
            turtlepos[1] += turtlepos[0]
            t.goto(0,turtlepos[1])
        turtlepos[0] = 0
        turtlepos[2] = 0
    t.goto(0,turtlepos[1])
    turtlepos[1] -= turtlepos[0]
    turtlepos[0] += 0.1







