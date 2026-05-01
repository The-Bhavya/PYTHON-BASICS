# star pattern

from turtle import *
s = Screen()
s.setup(400,400)
s.bgcolor('black')
pencolor('yellow')
for i in range(5):
    lt(72)
    for i in range(5):
        fd(100)
        rt(144)

mainloop()