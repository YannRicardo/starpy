from turtle import *
speed(3)
color('black', 'yellow')
begin_fill()
a = 72
b = 100
c = 2*a
t = True
right(a)
while True:
    forward(b)
    left(a) if t else right(c) # operador ternario
    t = not t
    if  abs(pos()) < 1:
        break
end_fill()
