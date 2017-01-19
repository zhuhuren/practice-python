from turtle import Turtle, Screen

def drawSpiral(lineLen, t):
    if lineLen > 0:
        t.forward(lineLen)
        t.right(90)
        drawSpiral(lineLen-5, t)

if __name__ == '__main__':
    t = Turtle()
    myWin = Screen()
    t.color('blue')
    drawSpiral(100, t)
    myWin.exitonclick()

