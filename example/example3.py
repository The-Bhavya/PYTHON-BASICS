#shell pattern with circles

from turtle import *
pencolor('dark blue')
pensize(2)
fillcolor('light blue')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()

mainloop()