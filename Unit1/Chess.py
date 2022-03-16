# boardlist1 = ["wr1","wh1","wb1","wk1","wq1","wb2","wh2","wr2"]
# boardlist2 = ["wp1","wp2","wp3","wp4","wp5","wp6","wp7","wp8"]
# boardlist3 = ["   ","   ","   ","   ","   ","   ","   ","   "]
# boardlist4 = ["   ","   ","   ","   ","   ","   ","   ","   "]
# boardlist5 = ["   ","   ","   ","   ","   ","   ","   ","   "]
# boardlist6 = ["   ","   ","   ","   ","   ","   ","   ","   "]
# boardlist7 = ["bp1","bp2","bp3","bp4","bp5","bp6","bp7","bp8"]
# boardlist8 = ["br1","bh1","bb1","bk1","bq1","bb2","bh2","br2"]
# def printboard():
#     print(boardlist1)
#     print(boardlist2)
#     print(boardlist3)
#     print(boardlist4)
#     print(boardlist5)
#     print(boardlist6)
#     print(boardlist7)
#     print(boardlist8)
#     print("")
# printboard()
# boardlist3[3] = boardlist2[3]
# boardlist2[3] =  "   "
# printboard()
import turtle
from turtle import *
screen = Screen() # create the screen
t = turtle.Turtle()

def move(x,y):
        for burtlez in screen.turtles():
            burtlez.onclick(screen.turtles()[0].goto)
def themove(x,y):




turtle1 = Turtle()
turtle2 = Turtle()
turtle1.goto(-50,-50)
turtle2.goto(50,50)
turtle1.onclick(move)
turtle2.onclick(move)
turtle.mainloop()


