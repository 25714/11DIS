import turtle as t

t.TurtleScreen
#move function
t.speed(0)
def penmove(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def circle_at_position_unfilled(x,y,rad,angle):
    penmove(x,y)
    t.circle(rad,angle)
#Make a filled in circle

def circle_at_position_filled(x,y,rad,colour,angle):
    penmove(x,y)
    t.fillcolor(colour)
    t.begin_fill()
    t.circle(rad,angle)
    t.end_fill()
def triangle_at_position_filled(x,y,s1,s2,s3,colour,angle1,angle2,angle3):
    penmove(x,y)
    t.fillcolor(colour)
    t.begin_fill()
    t.forward(s1)
    t.left(angle1)
    t.forward(s2)
    t.left(angle3)
    t.forward(s3)
    t.end_fill()
    t.seth(0)
#face
circle_at_position_filled(0,0,100,'#F2DF44', 360)
#eye1
circle_at_position_filled(-50,110,25,'black',360)
#iris1
circle_at_position_filled(-60,135,10, 'white',360)
circle_at_position_filled(-50,125,7, 'white',360)
#eye2
circle_at_position_filled(50,110,25,'black',360)
circle_at_position_filled(50,125,7, 'white',360)
#iris2
circle_at_position_filled(40,135,10, 'white',360)
#nose
triangle_at_position_filled(-10,110,20,20,20,'black',-120,-120,-120)
#rosy cheeks
circle_at_position_filled(-70,70,20,'#E16427',360)
circle_at_position_filled(70,70,20,'#E16427',360)
#mouth
circle_at_position_filled(0,40,20,'#F8654E',360)
t.getshapes()
#ears
triangle_at_position_filled(-90,180,45,90,90,'black',90,180,90)
t.seth(0)
t.ht()
t.Screen().exitonclick()


#bronze statue of hin in hospital bed with all of the ventilators. BUt has to be a trombone ventialtor, but hes like a sick trombone.
#Yeah.
