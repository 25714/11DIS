import turtle

unVar1 = 25
unVar2 = 100
unVar3 = 90
unVar4 = 150
unVar5 = -30
unVar6 = 75
unVar7 = 50

def polySquare(t, x, y, length):
    t.goto(x, y)
    t.setheading(270)

    t.begin_poly()

    for count in range(4):
        t.forward(length)
        t.left(90)

    t.end_poly()

    return t.get_poly()

def polyRectangle(t, x, y, length1, length2):
    t.goto(x, y)
    t.setheading(270)

    t.begin_poly()

    for count in range(2):
        t.forward(length1)
        t.left(90)
        t.forward(length2)
        t.left(90)

    t.end_poly()

    return t.get_poly()

def tankCursor():

    """
    Create the tank cursor.  An alternate solution is to toss the temporary turtle
    and use the commented out polygon assignments instead of the poly* function calls
    """

    temporary = turtle.Turtle()

    screen = turtle.getscreen()

    delay = screen.delay()

    screen.delay(0)

    temporary.hideturtle()
    temporary.penup()

    tank = turtle.Shape("compound")

    # tire1 = ((10, unVar1), (10, unVar1 - unVar6), (10 + 30, unVar1 - unVar6), (10 + 30, unVar1))
    tire1 = polyRectangle(temporary, 10, unVar1, unVar6, 30)  # Tire #1
    tank.addcomponent(tire1, "gray", "black")

    # tire2 = ((110, unVar1), (110, unVar1 - unVar6), (110 + 30, unVar1 - unVar6), (110 + 30, unVar1))
    tire2 = polyRectangle(temporary, 110, unVar1, unVar6, 30)  # Tire #2
    tank.addcomponent(tire2, "gray", "black")

    # tire3 = ((110, unVar2), (110, unVar2 - unVar6), (110 + 30, unVar2 - unVar6), (110 + 30, unVar2))
    tire3 = polyRectangle(temporary, 110, unVar2, unVar6, 30)  # Tire #3
    tank.addcomponent(tire3, "gray", "black")

    # tire4 = ((10, unVar2), (10, unVar2 - unVar6), (10 + 30, unVar2 - unVar6), (10 + 30, unVar2))
    tire4 = polyRectangle(temporary, 10, unVar2, unVar6, 30)  # Tire #4
    tank.addcomponent(tire4, "gray", "black")

    # bodyTank = ((20, unVar3), (20, unVar3 - 130), (20 + 110, unVar3 - 130), (20 + 110, unVar3))
    bodyTank = polyRectangle(temporary, 20, unVar3, 130, 110)
    tank.addcomponent(bodyTank, "black", "gray")

    # gunTank = ((65, unVar4), (65, unVar4 - 100), (65 + 20, unVar4 - 100), (65 + 20, unVar4))
    gunTank = polyRectangle(temporary, 65, unVar4, 100, 20)   # Gun
    tank.addcomponent(gunTank, "black", "gray")

    # exhaustTank = ((50, unVar5), (50, unVar5 - 20), (50 + 10, unVar5 - 20), (50 + 10, unVar5))
    exhaustTank = polyRectangle(temporary, 50, unVar5, 20, 10)
    tank.addcomponent(exhaustTank, "black", "gray")

    # turretTank = ((50, unVar7), (50, unVar7 - 50), (50 + 50, unVar7 - 50), (50 + 50, unVar7))
    turretTank = polySquare(temporary, 50, unVar7, 50)  # Turret
    tank.addcomponent(turretTank, "red", "gray")

    turtle.addshape("tank", shape=tank)
    del temporary

    screen.delay(delay)

tankCursor()  # creates and registers the "tank" cursor shape

turtle.shape("tank")

turtle.up()  # get rid of the ink

# show our tank in motion

turtle.setheading(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)

turtle.done()
