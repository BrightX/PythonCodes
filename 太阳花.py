from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
pensize(3) 
penup()
goto(0, -200)
pendown()
write('by 徐亮亮', font=("Bradley Hand ITC", 30, "bold"))
mainloop()    

done()
