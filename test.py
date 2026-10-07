from turtle import*
# ice cream

# cone
speed(10)
penup()
goto(0,-100)
pendown()
begin_fill()
color("chocolate")
goto(50,0)
goto(-50, 0)
goto(0,-100)
end_fill()

# Back scoop
penup()
goto(25,25)
left(90)
pendown()
color("#FFD1DB")
begin_fill()
circle(24)
end_fill()
penup()

# Right Scoop
begin_fill()
goto(50, 0)
pendown()
color("#B9EDD6")
circle(25 ,180)
left(90)
forward(50)
end_fill()

#Left Scoop
goto(0, 0)
left(90)
color("gold")
begin_fill()
circle(25,180)
end_fill()

left(125)
penup()
goto(0,-60)
stamp()
hideturtle()

done()