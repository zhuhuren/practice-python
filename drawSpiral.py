##import turtle
##myTurtle = turtle.Turtle()
##myWin = turtle.Screen()
##
##def drawSpiral(myTurtle, lineLen):
##    if lineLen > 0:
##        myTurtle.forward(lineLen)
##        myTurtle.right(90)
##        drawSpiral(myTurtle, lineLen -5)
##
##drawSpiral(myTurtle, 100)
##myWin.exitonclick()

##import turtle
##import random
##
##def tree(branchLen,t):
##    subtract = random.randint(5, 20)
##    angle = random.randint(5, 45)
##    if branchLen > 5:
##        scale = random.randint(9,11)
##        pen = branchLen // scale
##        if pen <=1: pen = 1
##        t.pensize(pen)
##        t.down()
##        t.color('black')
##        if branchLen - subtract <=5:
##            t.color('green')
##            t.pensize(7)
##        t.forward(branchLen)
##        t.right(angle)
##        tree(branchLen-subtract,t)
##        t.left(angle * 2)
##        tree(branchLen-subtract,t)
##        t.right(angle)
##        t.up()
##        t.backward(branchLen)
##
##def main():
##    t = turtle.Turtle()
##    myWin = turtle.Screen()
##    t.left(90)
##    t.up()
##    t.backward(300)
##    t.down()
##    t.color("black")
##    tree(105,t)
##    myWin.exitonclick()
##
##main()


import turtle

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-300,-150],[0,400],[300,-150]]
   sierpinski(myPoints,5,myTurtle)
   myWin.exitonclick()

main()
