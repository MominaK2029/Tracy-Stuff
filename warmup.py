#star imports everything
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
# create dictionary
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
# print out values in format (book : author)
# for key in book_list:
#     setposition(xposition1, yposition)
#     write(key, font = ("Courier", 14, "bold"))
#     while yposition >= 20:
#         yposition = yposition - 10

# for value in book_list:
#     setposition(xposition2, yposition2)
#     write(value, font = ("Courier", 14, "bold", "italic"))
#     while yposition2 >= 20:
#         yposition2 = yposition2 - 20
penup()
goto(-190, 160)
for index, (name, author) in enumerate(book_list.items()):
    penup()
    sety(160 - (index*80))
    write(f"{name} by {author}", font = ("Courier", 14, "bold"))

# stamping
goto(-220, -235)
stamp()
#Keeps window open
done()