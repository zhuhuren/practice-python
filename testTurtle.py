from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(400)
    left(175)
    if abs(pos()) < 1:
        break
end_fill()
done()
