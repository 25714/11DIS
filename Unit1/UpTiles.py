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


t.speed(0)
t.screensize(2000,2000,'white')
# t.setup( width = 600, height = 600, startx = None, starty = None)
t.setup(800, 600)
def uptiles(num1,num2):
    size = GCD(num1,num2)
    t.goto(num1/2,0)
    t.write(num1)
    t.goto(num1,0)
    t.goto(num1,-num2/2)
    t.write(num2)
    t.goto(num1,-num2)
    t.goto(0,-num2)
    t.goto(0,0)
    t.write(size)
    xcoord = 0
    ycoord = 0
    for i in range(int(num2/size)):
        for i in range(0,int(num1/size)):
            mysqaure(size)
            xcoord += size
            t.goto(xcoord,ycoord)
        xcoord = 0
        ycoord -= size
        t.penup()
        t.goto(xcoord,ycoord)
        t.pendown()
uptiles(400,300)
t.ht()
t.Screen().exitonclick()


