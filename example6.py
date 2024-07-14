# A  flower with petals

from turtle import *
s = Screen()
s.setup(500,500)
fillcolor('red')
pencolor('red')
for i in range(5):
    lt(72)
    penup()
    fd(80)
    pendown()
    begin_fill()
    circle(40)
    end_fill()
    penup()
    bk(80)
    pendown()

mainloop()
