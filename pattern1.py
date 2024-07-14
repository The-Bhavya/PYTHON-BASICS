from turtle import * 
speed("fastest")

# making a hexagon using for loop 
s = 6
d = 100
for i in range(s):
    fd(100)
    lt(360/s)
    write(i, font=('Arial', 12, 'normal'))
    circle(360/s)

mainloop()
