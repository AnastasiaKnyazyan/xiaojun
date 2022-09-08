from curses import COLOR_CYAN
from turtle import *

#making a house with windows

#drawing a square
speed(5)
width(10)
color("blue")
forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90)

forward(100)



#end of square

#drawing a door

color("green")
begin_fill()
left(90)
forward(130)
right(90)
forward(100)
right(90)
forward(130)
end_fill()
#making a roof
penup()
goto(300, 300)
pendown()

color("purple")
begin_fill()
right(150)
forward(300)
left(120)
forward(300)
end_fill()

#making a window
color("cyan")
begin_fill()
penup()
goto(100, 150)
pendown()
right(150)
forward(80)
right(90)
forward(100)
right(90)
forward(80)
right(90)
forward(100)
end_fill()
exitonclick()