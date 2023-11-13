"""Pracricing with Turtle."""
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()

idx = 0
leo.penup()
leo.goto(-120, -60)
leo.pendown()

colormode(255)
leo.color(32, 67, 93)

leo.begin_fill()
leo.speed(50)
leo.hideturtle()

leo_side_length: int = 400

while idx < 3:
    leo.forward(400)
    leo.left(120)
    idx += 1
leo.end_fill()

bob_side_length: int = 400

bob.penup()
bob.speed(30)
bob.goto(-120, -60)
bob.pendown()
bob.pencolor("pink")
bob.hideturtle()

idx_bob = 0
while idx_bob < 75:
    bob.forward(bob_side_length)
    bob.left(121.5)
    idx_bob += 1
    bob_side_length *= 0.965

done()