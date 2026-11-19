from turtle import*

bgcolor()

shape("turtle")
pensize(5)
speed("fastest")
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
    begin_fill()
    left(90)
    forward(120)
    left(90)
    forward(100)
    left(90)
    forward(120)
    left(90)
    forward(100)
    penup()
    end_fill()
    
    

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

item2 = 0

x2 = -185
y2 = 110

rectangle(-190, 190)
rectangle(-60, 190)
rectangle(70, 190)
rectangle(-190, 60)
rectangle(-60, 60)


color("white")
goto(-190, 160)

item = 0

x = -185
y = 110

for index, (name, author) in enumerate(book_list.items()):
    penup()
    goto(x, y)
    write(f"{name} \n by \n {author}", font = ("Courier", 9, "bold"))
    item += 1
    if item % 3 == 0:
        x = -175
        y -= 110
    else:
        x += 140
hideturtle()
done()