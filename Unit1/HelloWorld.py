# print("Hello World")
# name = "Lucas"
# print("My Name is " + name + ".")
# teacher = "Mr Fenwickle"
# print(f"your teacher is {teacher}.")
# print("# Squares List - multi line version")
# squares = []
# for i in range(10):
#     squares.append(i**2)
# print(squares)
#
# print("#Squares - one line version")
# print([i**2 for i in range(10)])
# DECLARE Integer a = 5
# Declare integer b = 2
# DECALRE INeteger c = 3
# DECLARE INTEGER RESULT
# SET RESULT a+b*c
# Display result
#
# a = 5
# b = 2
# c = 3
# result = 0
# result = a+b*c
# print(result)
#
# Declare string favefood
# display what is the name of your favourite food
# input favouritefood
# display you favourite food is
# display fave food
# faveFood = ""
# print("What is the name of your favourite food")
# favfood = input()
# print("your favourite food is")
# print("favourite food")
# Declare string 1stprize
# display enter the award for first prize
# input 1stPrize
# display the first prie winner will recieve, first prize.
# 1stprize = ""
# print("enter the award for first prize")
# 1stprize = input()
# print("te 1st boi get", 1stprize)
# declare in low, int hihgh. av.
# display enter low
# input lowdisplay enet high
# input high
# se av to low+hig/2
# display av
# low = 1
# high = 2
# av = 1+2/2
# print(av)
# declare rm
# rm = input
# print rmlength
# rm = 12
# print(len(rm))


# Declare Name
# Decalre Address
# Declare Number
# Declare wantJob
# DISPLAY "Your name is", name
# DISPLAY "Your adress is", address
# DISPLAY "Your number is", Number
# DISPLAY "Your wantJOb is", wantJOb
# name = "Lucas"
# address = "no"
# number = "420"
# wantjob = "america"
# print("Your name is", name)
# print("Your address is", address, "way")
# print("Your address is" + address + "way")
# print(f"You address is {address} way")
# print("Your number is", number)
# print("Your wantJOb is", wantjob)

# Declare totalSales
# Declare profit
# Input TotalSale
# math profit = totalSale *0.23
# totalSale = int(input(("What where the total sales this year? ")))
# print("profit is $" + totalSale * 0.23)
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
turtle.speed(0)
turtle.penup()
turtle.begin_poly()
turtle.circle(33)
draw_rectangle(-40,-40,35,80)
turtle.end_poly()
pawn = turtle.get_poly()
register_shape("pawn",pawn)


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
piecemovecontainer = {}
def ping(x,y):
    for coordinate in boardlist:
        coordlist = coordinate.split(",")
        xcoord = int(coordlist[0])
        ycoord = int(coordlist[1])
        if xcoord-20.05 <= x <= xcoord+19.95:
            if ycoord-19.95 <= y <= ycoord+20.05:
                for key,value in piecemovecontainer.items(): #key is the turtle, value is its number
                    if checkpiece(piecetype(value),xcoord,ycoord,turtledict[value].split(",")[0],turtledict[value].split(",")[1]):
                        key.goto(xcoord,ycoord)
                        turtledict[value] = f"{xcoord},{ycoord}"
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
def checkpiece(piecetype,xcoord1,ycoord1,xcoord2,ycoord2):
    knightlist = ["-1,+2","+1,+2","-2,+1","+2,+1","-2,-1","+2,-1","-1,-2","+1,-2"]
    rooklist = ["1,0","2,0","3,0","4,0","5,0","6,0","7,0","-1,0","-2,0","-3,0","-4,0","-5,0","-6,0","-7,0","0,1","0,2","0,3","0,4","0,5","0,6","0,7","0,-1","0,-2","0,-3","0,-4","0,-5","0,-6","0,-7",]
    bishoplist = ['-1,1', '-2,2', '-3,3', '-4,4', '-5,5', '-6,6', '-7,7', '1,1', '2,2', '3,3', '4,4', '5,5', '6,6', '7,7', '-1,-1', '-2,-2', '-3,-3', '-4,-4', '-5,-5', '-6,-6', '-7,-7', '1,-1', '2,-2', '3,-3', '4,-4', '5,-5', '6,-6', '7,-7']
    queenlist = rooklist+bishoplist
    kinglist = ["1,1","0,1","-1,1","1,0","-1,0","-1,-1","0,-1","1,-1",]
    orderlist = [rooklist,knightlist,bishoplist,queenlist,kinglist]
    whitepawnlist = ["0,1","0,2","-1,1","1,1"]
    blackpawnlist = ["0,-1","0,-2","-1,-1","1,01"]
    pawnlists = [whitepawnlist,blackpawnlist]
    if piecetype >= 5:
        for group in pawnlists[piecetype-5]:
            key = pieceping(int(xcoord2),int(ycoord2))
            print(group.split(","))
            xdif = group.split(",")[0]
            ydif = group.split(",")[1]
            if int(xcoord1) == int(xcoord2) + int(xdif)*40:
                if int(ycoord1) == int(ycoord2) + int(ydif)*40:
                    if int(ydif)%2 == 0 and coordinatelist[key-65] == f"{xcoord2},{ycoord2}":
                        return True
                    elif int(ydif) == 1 or int(ydif) == -1:
                        return True
    else:
        for group in orderlist[piecetype]:
            print(group.split(","))
            xdif = group.split(",")[0]
            ydif = group.split(",")[1]
            if int(xcoord1) == int(xcoord2) + int(xdif)*40:
                if int(ycoord1) == int(ycoord2) + int(ydif)*40:
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
        print(i,num-65,typelist)
        if num-65 in typelist:
            print(i)
            return i
    return 5




screen = Screen() # create the screen
chessboard = 8*8

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
        turtle.color("yellow")
    else:
        turtle.color("brown")
    turtle.shape("square")
    turtle.resizemode("user")
    turtle.turtlesize(2,2,0)
    turtle.onclick(ping)
for i,turtle in enumerate(screen.turtles()[65:81]):
    turtle.speed(0)
    turtle.penup()
    turtle.shape("pawn")
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
    if ptype == 2:
        turtle.shape("bishop")
        turtle.turtlesize(0.18,0.18,0)
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

