from turtle import *
r = eval(input("请输入初始圆半径r:"))
s = r
n = int(input("请输入同心圆个数n:"))
for i in range(n):
    r = (i + 1)* s
    penup()
    goto(0, -r)
    pendown()
    circle(r)
