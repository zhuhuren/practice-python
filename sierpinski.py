from turtle import Turtle, Screen

def drawTriangle(points, col, t):
    pt1 = points[0]
    pt2 = points[1]
    pt3 = points[2]
    t.color(col)
    t.up()
    t.goto(pt1)
    t.down()
    t.begin_fill()
    t.goto(pt2)
    t.goto(pt3)
    t.goto(pt1)
    t.end_fill()

def midPT(pt1, pt2):
    return [(pt1[0] + pt2[0]) / 2, (pt1[1] + pt2[1]) / 2]

def sierpinski(points, degree, t):
    colors = ['red', 'yellow', 'blue', 'green', 'cyan', 'magenta', 'brown', 'orange', 'white', 'black']
    drawTriangle(points, colors[degree], t)
    pt1 = points[0]
    pt2 = points[1]
    pt3 = points[2]
    mid1 = midPT(pt1, pt2)
    mid2 = midPT(pt2, pt3)
    mid3 = midPT(pt3, pt1)
    if degree > 0:
        sierpinski([pt1, mid1, mid3], degree-1, t)
        sierpinski([pt2, mid2, mid1], degree-1, t)
        sierpinski([pt3, mid3, mid2], degree-1, t)

if __name__ == '__main__':
    points = [[-200, -100], [200, -100], [0, 200]]
    t = Turtle()
    myWin = Screen()
##    drawTriangle(points, 'blue', t)
    t.speed(200)
    sierpinski(points, 4, t)
    myWin.exitonclick()
    
