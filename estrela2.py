from turtle import *
speed(3)
color('black', 'yellow')
begin_fill()
a = 72
b = 100
c = 144
right(a)
while True:
    forward(b)
    left(a)
    forward(b)
    right(c)
    if  abs(pos()) < 1:
        break
end_fill()
