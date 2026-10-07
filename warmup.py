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

# Rounded tops
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

# create dictionary
book_list = {
    "The Alchemyst" : "Michael Scott",
    "Kane Chronicles" : "Rick Riordan",
    "Once Upon a Heart" : "Stephanie Garber",
    "A Study in Drowning" : "Ava Reid",
    "What The River Knows" : "Isabel Ibañez",
}
# print out values in format (book : author)
# for i in book_list:
#     print([key], "by" [value])
# spacing 

# stamping
goto(-250, -240)
stamp()
#Keeps window open
done()