#concentric circles

from turtle import *
s = Screen()
s.setup(1000,700)
colors = ['red', 'light pink']
pencolor('black')
pensize(2)
for i in range (6,0,-1):
    penup()
    setpos(0,-20*i)
    pendown()
    fillcolor(colors[i%2])
    begin_fill()
    circle(20*i)
    end_fill()

mainloop()
