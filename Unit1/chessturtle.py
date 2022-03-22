import turtle
from turtle import *
def draw_rectangle(x, y, length1, length2):
    turtle.goto(x, y)
    turtle.setheading(270)
    for count in range(1):
        turtle.forward(length1)
        turtle.left(90)
        turtle.forward(length2)
        turtle.left(90)
    turtle.forward(length1)
    turtle.left(90)
    turtle.goto(0,0)
#PAWN
turtle.speed(0)
turtle.penup()
turtle.begin_poly()
turtle.circle(33)
draw_rectangle(-40,-40,35,80)
turtle.end_poly()
pawn = turtle.get_poly()
register_shape("pawn",pawn)

##ROOK
turtle.reset()
turtle.speed(0)
turtle.penup()
turtle.goto(-50,50)
turtle.begin_poly()
turtle.speed(0)
for i in range(3):
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    if i <=1:
     turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.goto(50,-60)
turtle.left(90)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.goto(-30,30)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.end_poly()
r = turtle.get_poly()
register_shape("rook",r)

#BISHOP
turtle.reset()
turtle.penup()
turtle.goto(-30,-60)
turtle.begin_poly()
turtle.speed(20)
turtle.right(50)
turtle.circle(80,-110,50)
turtle.circle(-10)
turtle.left(40)
turtle.goto(-15,20)
turtle.goto(-5,20)
turtle.goto(10,60)
turtle.right(90)
turtle.circle(80,-90,50)
turtle.right(60)
turtle.forward(30)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(140)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(50)
b = turtle.get_poly()
turtle.register_shape("bishop",b)
turtle.penup()
turtle.goto(0,0)

#KING
turtle.reset()
turtle.speed(0)
turtle.penup()
turtle.goto(40,-70)
turtle.begin_poly()
turtle.goto(-60,-70)
turtle.circle(10,-180)
turtle.goto(-50,-50)
turtle.goto(-70,10)
turtle.left(120)
turtle.circle(20,-180)
turtle.right(180)
turtle.forward(5)
turtle.left(50)
turtle.forward(20)
turtle.left(100)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(20)
turtle.left(100)
turtle.forward(20)
turtle.left(60)
turtle.circle(-20,180)
turtle.forward(66)
turtle.left(110)
turtle.forward(10)
turtle.circle(-10,180)
turtle.forward(12)
turtle.end_poly()
k = turtle.get_poly()
turtle.register_shape("king",k)

#QUEEN
turtle.reset()
turtle.penup()
turtle.speed(0)
turtle.goto(0,-70)
turtle.begin_poly()
turtle.right(180)
turtle.forward(50)
turtle.right(90)
turtle.forward(20)
xcoord = -50
ycoord = 30
turtle.right(75)
turtle.goto(-100,50)
turtle.circle(15)
turtle.goto(-50,10)
turtle.right(15)
turtle.goto(xcoord,ycoord+40)
turtle.circle(15)
turtle.goto(xcoord+40,ycoord-20)
xcoord+=40
turtle.goto(xcoord+40,ycoord+40)
turtle.circle(15)
turtle.goto(xcoord+40,ycoord-20)
turtle.goto(80,50)
turtle.right(15)
turtle.circle(15)
turtle.goto(xcoord+40,-50)
turtle.goto(xcoord+40,-70)
turtle.goto(0,-70)
turtle.end_poly()
q = turtle.get_poly()
turtle.register_shape("queen",q)
turtle.goto(0,0)

#KNight
turtle.reset()
turtle.penup()
turtle.speed(0)
turtle.goto(0,-80)
turtle.begin_poly()
turtle.goto(-50,-80)
turtle.goto(-50,-60)
turtle.left(70)
turtle.circle(50,30)
turtle.left(20)
turtle.circle(-120,30)
turtle.circle(-60,90)
turtle.forward(20)
turtle.right(180)
turtle.forward(20)
turtle.right(120)
turtle.forward(40)
turtle.right(70)
turtle.forward(5)
turtle.right(70)
turtle.forward(35)
turtle.left(60)
turtle.forward(70)
turtle.circle(-10,90)
turtle.forward(30)
turtle.circle(-10,90)
turtle.forward(30)
turtle.circle(50,20)
turtle.circle(-50,50)
turtle.left(160)
turtle.circle(180,30)
turtle.right(40)
turtle.forward(50)
turtle.goto(-50,-80)
turtle.reset()
turtle.end_poly()
kn = turtle.get_poly()
turtle.register_shape("knight",kn)
turtle.reset()
piecemovecontainer = {}
piecemovedlist = []
def ping(x,y):
    for coordinate in boardlist:
        coordlist = coordinate.split(",")
        xcoord = int(coordlist[0])
        ycoord = int(coordlist[1])
        if xcoord-20.05 <= x <= xcoord+19.95:
            if ycoord-19.95 <= y <= ycoord+20.05:
                for key,value in piecemovecontainer.items(): #key is the turtle, value is its number
                    if checkpiece(piecetype(value),xcoord,ycoord,turtledict[value].split(",")[0],turtledict[value].split(",")[1],value):
                        key.goto(xcoord,ycoord)
                        turtledict[value] = f"{xcoord},{ycoord}"
                        piecemovedlist.append(value)
                        print(piecemovedlist)
                        checktakepiece(value)
                    if value >= 81:
                        key.color("white")
                    else:
                        key.color("black")
    piecemovecontainer.clear()
def pieceping(x,y):
    for key,value in turtledict.items():
        coordlist = value.split(",")
        xcoord = int(coordlist[0])
        ycoord = int(coordlist[1])
        if xcoord-20 <= x <= xcoord+20:
            if ycoord-20 <= y <= ycoord+20:
                for turtnumber,turt in enumerate(screen.turtles()):
                    if turtnumber == key:
                        turt.color("red")
                        piecemovecontainer[turt] = key
                        return key
def checkpiece(piecetype,xcoord1,ycoord1,xcoord2,ycoord2,piece):
    knightlist = ["-1,+2","+1,+2","-2,+1","+2,+1","-2,-1","+2,-1","-1,-2","+1,-2"]
    rooklist = ["1,0","2,0","3,0","4,0","5,0","6,0","7,0","-1,0","-2,0","-3,0","-4,0","-5,0","-6,0","-7,0","0,1","0,2","0,3","0,4","0,5","0,6","0,7","0,-1","0,-2","0,-3","0,-4","0,-5","0,-6","0,-7",]
    bishoplist = ['-1,1', '-2,2', '-3,3', '-4,4', '-5,5', '-6,6', '-7,7', '1,1', '2,2', '3,3', '4,4', '5,5', '6,6', '7,7', '-1,-1', '-2,-2', '-3,-3', '-4,-4', '-5,-5', '-6,-6', '-7,-7', '1,-1', '2,-2', '3,-3', '4,-4', '5,-5', '6,-6', '7,-7']
    queenlist = rooklist+bishoplist
    kinglist = ["1,1","0,1","-1,1","1,0","-1,0","-1,-1","0,-1","1,-1","+2,0","-2,0"]
    orderlist = [rooklist,knightlist,bishoplist,queenlist,kinglist]
    whitepawnlist = ["0,1","0,2","-1,1","1,1"]
    blackpawnlist = ["0,-1","0,-2","-1,-1","1,-1"]
    pawnlists = [whitepawnlist,blackpawnlist]
    newmoveslist = []
    if piecetype >= 5:
        for group in pawnlists[piecetype-5]:
            key = pieceping(int(xcoord2),int(ycoord2))
            xdif = group.split(",")[0]
            ydif = group.split(",")[1]
            newxcoord = int(xcoord2) + int(xdif)*40
            newycoord = int(ycoord2) + int(ydif)*40
            if int(xcoord1) == newxcoord:
                if int(ycoord1) == newycoord:
                    if int(ydif)%2 == 0 and coordinatelist[key-65] == f"{xcoord2},{ycoord2}":
                        return True
                    elif int(ydif) == 1 or int(ydif) == -1:
                        if int(xdif) == 1 or int(xdif) == -1:
                            print(f"{newxcoord},{newycoord}")
                            print(turtledict.items())
                            for i,v in turtledict.items():
                                if f"{newxcoord},{newycoord}" == v:
                                    return True
                        else:
                            return True
    else:
        for i,group in enumerate(orderlist[piecetype]):
            xdif = group.split(",")[0]
            ydif = group.split(",")[1]
            if int(xcoord1) == int(xcoord2) + int(xdif)*40:
                if int(ycoord1) == int(ycoord2) + int(ydif)*40:
                    if orderlist[piecetype] == kinglist:
                        if int(xdif)%2 == 0:
                            if not piece in piecemovedlist and not piece-4 in piecemovedlist and not piece+3 in piecemovedlist:
                                return True
                        elif int(xdif) == 1 or int(xdif) == -1:
                            return True
                    if orderlist[piecetype] == rooklist:
                        if i <=6:
                            print(1)
                            return True
                        elif i > 7 and i<=13:
                            print(2)
                            return True
                        elif i > 13 and i<=20:
                            print(3)
                            return True
                        elif i >20:
                            print(4)
                            return True

                    else:
                        return True
def checklineofsight():
    return(False)

def checkenpassant():
    return True

def piecetype(num):
    rooklist = [0,7,24,31]
    knightlist = [1,6,25,30]
    bishoplist = [2,5,26,29]
    queenlist = [3,27]
    kinglist = [4,28]
    blackpawnlist = [8,9,10,11,12,13,14,15]
    whitepawnlist = [16,17,18,19,20,21,22,23]
    pieceslist = [rooklist,knightlist,bishoplist,queenlist,kinglist,whitepawnlist,blackpawnlist]
    for i,typelist in enumerate(pieceslist):
        if num-65 in typelist:
            return i
    return 5
def checktakepiece(colour):
    if colour >= 81:
        colour = "white"
    else:
        colour = "black"
    for index,key in enumerate(turtledict.items()):
        if index <= 15:
            for index2,key2 in enumerate(turtledict.items()):
                if index2> 15:
                    if key[1] == key2[1]:
                        for i,v in enumerate(screen.turtles()):
                            if colour == "white":
                                print(i,key[0])
                                if i == key[0]:
                                    v.goto(-350,-350)
                                    turtledict[i] = f"{-2000},{-2000}"
                            if colour == "black":
                                if i == key2[0]:
                                    v.goto(-350,-350)
                                    turtledict[i] = f"-2000,-2000"

screen = Screen() # create the screen
turtle1 = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
turtle4 = Turtle()
turtle5 = Turtle()
turtle6 = Turtle()
turtle7 = Turtle()
turtle8 = Turtle()
turtle9 = Turtle()
turtle10 = Turtle()
turtle11 = Turtle()
turtle12 = Turtle()
turtle13 = Turtle()
turtle14 = Turtle()
turtle15 = Turtle()
turtle16 = Turtle()
turtle17 = Turtle()
turtle18 = Turtle()
turtle19 = Turtle()
turtle20 = Turtle()
turtle21 = Turtle()
turtle22 = Turtle()
turtle23 = Turtle()
turtle24 = Turtle()
turtle25 = Turtle()
turtle26 = Turtle()
turtle27 = Turtle()
turtle28 = Turtle()
turtle29 = Turtle()
turtle30 = Turtle()
turtle31 = Turtle()
turtle32 = Turtle()
turtle33 = Turtle()
turtle34 = Turtle()
turtle35 = Turtle()
turtle36 = Turtle()
turtle37 = Turtle()
turtle38 = Turtle()
turtle39 = Turtle()
turtle40 = Turtle()
turtle41 = Turtle()
turtle42 = Turtle()
turtle43 = Turtle()
turtle44 = Turtle()
turtle45 = Turtle()
turtle46 = Turtle()
turtle47 = Turtle()
turtle48 = Turtle()
turtle49 = Turtle()
turtle50 = Turtle()
turtle51 = Turtle()
turtle52 = Turtle()
turtle53 = Turtle()
turtle54 = Turtle()
turtle55 = Turtle()
turtle56 = Turtle()
turtle57 = Turtle()
turtle58 = Turtle()
turtle59 = Turtle()
turtle60 = Turtle()
turtle61 = Turtle()
turtle62 = Turtle()
turtle63 = Turtle()
turtle64 = Turtle()
turtle65 = Turtle()
turtle66 = Turtle()
turtle67 = Turtle()
turtle68 = Turtle()
turtle69 = Turtle()
turtle70 = Turtle()
turtle71 = Turtle()
turtle72 = Turtle()
turtle73 = Turtle()
turtle74 = Turtle()
turtle75 = Turtle()
turtle76 = Turtle()
turtle77 = Turtle()
turtle78 = Turtle()
turtle79 = Turtle()
turtle80 = Turtle()
turtle81 = Turtle()
turtle82 = Turtle()
turtle83 = Turtle()
turtle84 = Turtle()
turtle85 = Turtle()
turtle86 = Turtle()
turtle87 = Turtle()
turtle88 = Turtle()
turtle89 = Turtle()
turtle90 = Turtle()
turtle91 = Turtle()
turtle92 = Turtle()
turtle93 = Turtle()
turtle94 = Turtle()
turtle95 = Turtle()
turtle96 = Turtle()
turtleindex = 0
for i,turtle in enumerate(screen.turtles()[0:64]):
    turtle.speed(0)
    turtle.penup()
    if i%8 == 0 and i != 0:
        turtleindex+=1
    if (turtleindex+i)%2 == 0:
        turtle.color("#FADA66")
    else:
        turtle.color("#5B3601")
    turtle.shape("square")
    turtle.resizemode("user")
    turtle.turtlesize(2,2,0)
    turtle.onclick(ping)
for i,turtle in enumerate(screen.turtles()[65:81]):
    turtle.speed(0)
    turtle.penup()
    ptype = piecetype(i+65)
    if ptype >= 5:
        turtle.shape("pawn")
        turtle.turtlesize(0.2,0.2,0)
    if ptype == 0:
        turtle.shape("rook")
        turtle.turtlesize(0.2,0.2,0)
    if ptype == 1:
        turtle.shape("knight")
        turtle.turtlesize(0.18,0.18,0)
    if ptype == 2:
        turtle.shape("bishop")
        turtle.turtlesize(0.18,0.18,0)
    if ptype == 3:
        turtle.shape("queen")
        turtle.turtlesize(0.15,0.15,0)
    if ptype == 4:
        turtle.shape("king")
        turtle.turtlesize(0.2,0.2,0)
    turtle.color("black")
    turtle.resizemode("user")
    turtle.turtlesize(0.2,0.2,0)
    turtle.left(90)
    turtle.onclick(pieceping)
for i,turtle in enumerate(screen.turtles()[81:97]):
    turtle.speed(0)
    turtle.penup()
    ptype = piecetype(i+81)
    if ptype >= 5:
        turtle.shape("pawn")
        turtle.turtlesize(0.2,0.2,0)
    if ptype == 0:
        turtle.shape("rook")
        turtle.turtlesize(0.2,0.2,0)
    if ptype == 1:
        turtle.shape("knight")
        turtle.turtlesize(0.18,0.18,0)
    if ptype == 2:
        turtle.shape("bishop")
        turtle.turtlesize(0.18,0.18,0)
    if ptype == 3:
        turtle.shape("queen")
        turtle.turtlesize(0.15,0.15,0)
    if ptype == 4:
        turtle.shape("king")
        turtle.turtlesize(0.2,0.2,0)

    turtle.color("white")
    turtle.resizemode("user")
    turtle.left(90)
    turtle.onclick(pieceping)

coordinatelist =[]
boardlist = []
ycoord = 150
xcoord = -150
index = 0
for i in range(8):
        for turtle in screen.turtles()[index:index+8]:
            boardlist.append(f"{xcoord},{ycoord}")
            turtle.goto(xcoord,ycoord)
            xcoord += 40
        index+=8
        xcoord = -150
        ycoord -= 40
ycoord = 150
xcoord = -150
index = 65
for i in range(2):
    for turtle in screen.turtles()[index:index+8]:
            coordinatelist.append(f"{xcoord},{ycoord}")
            turtle.goto(xcoord,ycoord)
            xcoord += 40
    index+=8
    xcoord = -150
    ycoord -= 40
ycoord = -90
xcoord = -150
index = 81
for i in range(2):
    for turtle in screen.turtles()[index:index+8]:
            coordinatelist.append(f"{xcoord},{ycoord}")
            turtle.goto(xcoord,ycoord)
            xcoord += 40
    index+=8
    xcoord = -150
    ycoord -= 40
turtledict = {}
print(coordinatelist)
for i in range(32):
    turtledict[i+65] = coordinatelist[i]
print(turtledict)
screen.mainloop() # start everything runnin
