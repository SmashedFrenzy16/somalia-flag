from turtle import *

shape("arrow")
speed(2)
up()
goto(-50,0)
down()
bgcolor("dodgerblue")
color("white")
begin_fill()

for i in range(5):
    forward(100)
    right(144)

end_fill()
hideturtle()
