from turtle import*

bgcolor()

shape("turtle")
pensize(5)
speed(10)
penup()
goto(-240, -270)
pendown()
color("#c7e4ff")
begin_fill()
#square
for i in range (2):
    forward(500)
    left(90)
    forward(550)
    left(90)
end_fill()
penup()
#Messages Writing
color("Black")
goto(-210, 220)
write("Lillian's Book Shelf", font = ("Courier", 28, "bold"))

# Rounded Bottom
goto(-240, -270)
pendown()
color("#42679E")
begin_fill()
circle(10, -180)
left(180)
forward(500)
right(180)
circle(10, -180)
left(180)
forward(500)
end_fill()
penup()

# Rounded Top
goto(-240, 280)
pendown()
color("#42679E")
begin_fill()
left(180)
circle(10, -180)
right(180)
forward(500)
left(180)
circle(10, -180)
right(180)
forward(500)
end_fill()
penup()

def rectangle(x, y):
    goto(x, y)
    pendown()
    left(90)
    forward(50)
    left(90)
    forward(30)
    left(90)
    forward(50)
    left(90)
    forward(30)
    penup()
rectangle(-210, 160)
    

book_list = {
    "The Alchemyst" : "M. Scott",
    "Kane Chronicles" : "R. Riordan",
    "Once Upon a Heart" : "S. Garber",
    "You've reached Sam" : "D. Thao",
    "What The River Knows" : "I. Ibañez",
}
xposition1 = -210
xposition2 = 40
yposition = 120
yposition2 = 120
line_space = 40

penup()
goto(-190, 160)
for index, (name, author) in enumerate(book_list.items()):
    penup()
    sety(160 - (index*80))
    write(f"{name} by {author}", font = ("Courier", 10, "bold"))


done()
hideturtle()