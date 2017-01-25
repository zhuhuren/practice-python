from turtle import Turtle, Screen

def tree(lineLen, t):
    from random import randint
    
    if lineLen > 5:
        angle1 = randint(5, 45)
        angle2 = randint(5, 45)
        lenDecrease = randint(10, 15)
        t.color('black')
        pen = lineLen // 8
        if pen == 0: pen = 1
        if lineLen - lenDecrease <= 5:
            t.color('green')
            pen = 5
        t.pensize(pen)
        t.down()
        t.forward(lineLen)
        t.right(angle1)
        tree(lineLen-lenDecrease, t)
        t.left(angle1 + angle2)
        tree(lineLen-lenDecrease, t)
        t.right(angle2)
        t.up()
        t.backward(lineLen)

if __name__ == '__main__':
    t = Turtle()
    myWin = Screen()
    t.color('green')
    t.speed(100)
    t.left(90)
    t.up()
    t.goto(0, -300)
    t.down()
    tree(120, t)
    myWin.exitonclick()
